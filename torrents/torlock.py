import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
from helper.asyncioPoliciesFix import decorator_asyncio_fix
import re
from helper.html_scraper import Scraper


class Torlock:

    def __init__(self):
        self.BASE_URL = 'https://www.torlock.com'

    @decorator_asyncio_fix
    async def _individual_scrap(self, session, url, obj):
        try:
            async with session.get(url) as res:
                html = await res.text(encoding="ISO-8859-1")
                soup = BeautifulSoup(html, 'lxml')
                try:
                    tm = soup.find_all('a')
                    magnet = tm[20]['href']
                    torrent = tm[23]['href']
                    try:
                        obj['poster'] = soup.find_all(
                            'img', class_='img-responsive')[0]['src']
                    except:
                        pass
                    if str(magnet).startswith('magnet') and str(torrent).endswith('torrent'):
                        obj['torrent'] = torrent
                        obj['magnet'] = magnet
                        obj['hash'] = re.search(
                            r'([{a-f\d,A-F\d}]{32,40})\b', magnet).group(0)
                        obj['category'] = tm[25].text
                        imgs = soup.select('.tab-content img.img-fluid')
                        if imgs and len(imgs) > 0:
                            obj['screenshot'] = [img['src'] for img in imgs]
                    else:
                        del obj
                except IndexError:
                    pass
        except:
            return None

    async def _get_torrent(self, result, session, urls):
        tasks = []
        for idx, url in enumerate(urls):
            for obj in result['data']:
                if obj['url'] == url:
                    task = asyncio.create_task(self._individual_scrap(
                        session, url, result['data'][idx]))
                    tasks.append(task)
        await asyncio.gather(*tasks)
        return result

    def _parser(self, htmls, is_trending=False):
        try:
            idx = 5
            if is_trending:
                idx = 1
            for html in htmls:
                soup = BeautifulSoup(html, 'lxml')
                list_of_urls = []
                my_dict = {
                    'data': []
                }
                tr = soup.find_all('tr')
                for tr in soup.find_all('tr')[idx:]:
                    td = tr.find_all("td")
                    name = td[0].get_text(strip=True)
                    if name != '':
                        url = td[0].find('a')['href']
                        if url == '':
                            break
                        url = self.BASE_URL + url
                        list_of_urls.append(url)
                        size = td[2].get_text(strip=True)
                        date = td[1].get_text(strip=True)
                        seeders = td[3].get_text(strip=True)
                        leechers = td[4].get_text(strip=True)
                        my_dict['data'].append({
                            'name': name,
                            'size': size,
                            'date': date,
                            'seeders': seeders,
                            'leechers': leechers,
                            'url': url,
                        })
                try:
                    ul = soup.find('ul', class_='pagination')
                    tpages = ul.find_all('a')[-2].text
                    current_page = (
                        ul.find('li', class_='active')).find('span').text.split(' ')[0]
                    my_dict['current_page'] = int(current_page)
                    my_dict['total_pages'] = int(tpages)
                except:
                    my_dict['current_page'] = None
                    my_dict['total_pages'] = None
                return my_dict, list_of_urls
        except:
            return None, None

    async def search(self, query, page):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            url = self.BASE_URL + \
                "/all/torrents/{}.html?sort=seeds&page={}".format(query, page)
            return await self.parser_result(start_time, url, session)

    async def parser_result(self, start_time, url, session, is_trending=False):
        htmls = await Scraper().get_all_results(session, url)
        result, urls = self._parser(htmls, is_trending)
        if result != None:
            results = await self._get_torrent(result, session, urls)
            results['time'] = time.time() - start_time
            results['total'] = len(results['data'])
            return results
        return result

    async def trending(self, category, page):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            if not category:
                url = self.BASE_URL + '/top100.html'
            else:
                if category == 'books':
                    category = 'ebooks'
                url = self.BASE_URL + \
                    "/{}.html".format(category.lower())
            return await self.parser_result(start_time, url, session, is_trending=True)

    async def recent(self, category, page):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            if not category:
                url = self.BASE_URL + '/fresh.html'
            else:
                if category == 'books':
                    category = 'ebooks'
                url = self.BASE_URL + \
                    "/{}/{}/added/desc.html".format(category, page)
            return await self.parser_result(start_time, url, session, is_trending=True)

    #! Maybe impelment Search By Category in Future
