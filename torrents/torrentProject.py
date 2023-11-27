import asyncio
import time
import aiohttp
import requests
from bs4 import BeautifulSoup
from helper.asyncioPoliciesFix import decorator_asyncio_fix
from helper.html_scraper import Scraper
from constants.base_url import TORRENTPROJECT
from constants.headers import HEADER_AIO


class TorrentProject:
    def __init__(self):
        self.BASE_URL = TORRENTPROJECT
        self.LIMIT = None

    @decorator_asyncio_fix
    async def _individual_scrap(self, session, url, obj, sem):
        async with sem:
            try:
                async with session.get(
                    url,
                    headers=HEADER_AIO,
                ) as res:
                    html = await res.text(encoding="ISO-8859-1")
                    soup = BeautifulSoup(html, "html.parser")
                    try:
                        magnet = soup.select_one(
                            "#download > div:nth-child(2) > div > a"
                        )["href"]
                        index_of_magnet = magnet.index("magnet")
                        magnet = requests.utils.unquote(magnet[index_of_magnet:])
                        obj["magnet"] = magnet
                    except:
                        ...
            except:
                return None

    async def _get_torrent(self, result, session, urls):
        tasks = []
        sem = asyncio.Semaphore(3)
        for idx, url in enumerate(urls):
            for obj in result["data"]:
                if obj["url"] == url:
                    task = asyncio.create_task(
                        self._individual_scrap(session, url, result["data"][idx], sem)
                    )
                    tasks.append(task)
        await asyncio.gather(*tasks)
        return result

    def _parser(self, htmls):
        try:
            for html in htmls:
                soup = BeautifulSoup(html, "html.parser")
                list_of_urls = []
                my_dict = {"data": []}
                for div in soup.select("div#similarfiles div")[2:]:
                    span = div.find_all("span")
                    name = span[0].find("a").text
                    url = self.BASE_URL + span[0].find("a")["href"]
                    list_of_urls.append(url)
                    seeders = span[2].text
                    leechers = span[3].text
                    date = span[4].text
                    size = span[5].text

                    my_dict["data"].append(
                        {
                            "name": name,
                            "size": size,
                            "date": date,
                            "seeders": seeders,
                            "leechers": leechers,
                            "url": url,
                        }
                    )
                    if len(my_dict["data"]) == self.LIMIT:
                        break
                return my_dict, list_of_urls
        except:
            return None, None

    async def search(self, query, page, limit):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            self.LIMIT = limit
            url = self.BASE_URL + "/?t={}&p={}".format(query, page - 1)
            return await self.parser_result(start_time, url, session)

    async def parser_result(self, start_time, url, session):
        htmls = await Scraper().get_all_results(session, url)
        result, urls = self._parser(htmls)
        if result is not None:
            results = await self._get_torrent(result, session, urls)
            results["time"] = time.time() - start_time
            results["total"] = len(results["data"])
            return results
        return result
