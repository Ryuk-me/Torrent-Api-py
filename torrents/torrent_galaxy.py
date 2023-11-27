import re
import time
import aiohttp
from bs4 import BeautifulSoup
from helper.html_scraper import Scraper
from constants.base_url import TGX


class TorrentGalaxy:
    def __init__(self):
        self.BASE_URL = TGX
        self.LIMIT = None

    def _parser_individual(self, html):
        try:
            soup = BeautifulSoup(html[0], "html.parser")
            my_dict = {"data": []}
            root_div = soup.find("div", class_="gluewrapper")
            post_nd_torrents = root_div.find_next("div").find_all("div")
            poster = post_nd_torrents[1].find("img")["data-src"]
            torrentsand_all = post_nd_torrents[4].find_all("a")
            torrent_link = torrentsand_all[0]["href"]
            magnet_link = torrentsand_all[1]["href"]
            direct_link = self.BASE_URL + torrentsand_all[2]["href"]

            details_root = soup.find("div", class_="gluewrapper").select(
                "div > :nth-child(2) > div > .tprow"
            )

            name = details_root[0].find_all("div")[-1].get_text(strip=True)
            category = (
                details_root[3].find_all("div")[-1].get_text(strip=True).split(">")[0]
            )
            languagee = details_root[4].find_all("div")[-1].get_text(strip=True)
            size = details_root[5].find_all("div")[-1].get_text(strip=True)
            hash = details_root[6].find_all("div")[-1].get_text(strip=True)
            username = (
                details_root[7]
                .find_all("div")[-1]
                .find("span", class_="username")
                .get_text(strip=True)
            )
            date_up = details_root[8].find_all("div")[-1].get_text(strip=True)

            btns = details_root[10].find_all("button")
            seeders = btns[0].find("span").get_text(strip=True)
            leechers = btns[1].find("span").get_text(strip=True)
            downloads = btns[2].find("span").get_text(strip=True)
            imdb_id = soup.select_one("#imdbpage")["href"].split("/")[-1]
            genre_list = [
                x.get_text(strip=True) for x in details_root[11].find_all("a")
            ]
            soup.find("div", id="intblockslide").find_all("a")
            imgs = [
                img["href"]
                for img in (soup.find("div", id="intblockslide").find_all("a"))
                if img["href"].endswith((".png", ".jpg", ".jpeg"))
            ]
            my_dict["data"].append(
                {
                    "name": name,
                    "size": size,
                    "seeders": seeders,
                    "language": languagee,
                    "leechers": leechers,
                    "category": category,
                    "uploader": username,
                    "downloads": downloads,
                    "poster": poster,
                    "direct_download_link": direct_link,
                    "imdb_id": imdb_id,
                    "hash": hash,
                    "magnet": magnet_link,
                    "torrent": torrent_link,
                    "screenshot": imgs,
                    "genre": genre_list,
                    "date": date_up,
                }
            )
            return my_dict
        except:
            return None

    def _parser(self, htmls):
        try:
            for html in htmls:
                soup = BeautifulSoup(html, "html.parser")

                my_dict = {"data": []}
                for idx, divs in enumerate(soup.find_all("div", class_="tgxtablerow")):
                    div = divs.find_all("div")
                    try:
                        name = div[4].find("a").get_text(strip=True)
                        imdb_url = (div[4].find_all("a"))[-1]["href"]
                    except:
                        name = (div[1].find("a", class_="txlight")).find("b").text
                        imdb_url = (div[1].find_all("a"))[-1]["href"]

                    if name != "":
                        try:
                            magnet = div[5].find_all("a")[1]["href"]
                            torrent = div[5].find_all("a")[0]["href"]
                        except:
                            magnet = div[3].find_all("a")[1]["href"]
                            torrent = div[3].find_all("a")[0]["href"]
                        size = soup.select("span.badge.badge-secondary.txlight")[
                            idx
                        ].text
                        try:
                            url = div[4].find("a")["href"]
                        except:
                            url = div[1].find("a", class_="txlight")["href"]
                        try:
                            date = div[12].get_text(strip=True)
                        except:
                            date = div[10].get_text(strip=True)
                        try:
                            seeders_leechers = div[11].find_all("b")
                            seeders = seeders_leechers[0].text
                            leechers = seeders_leechers[1].text
                        except:
                            seeders_leechers = div[11].find_all("b")
                            seeders = seeders_leechers[0].text
                            leechers = seeders_leechers[1].text
                        try:
                            uploader = (div[7].find("a")).find("span").text
                        except:
                            uploader = (div[5].find("a")).find("span").text
                        try:
                            category = (
                                div[0].find("small").text.replace("&nbsp", "")
                            ).split(":")[0]
                        except:
                            category = None
                        my_dict["data"].append(
                            {
                                "name": name,
                                "size": size,
                                "seeders": seeders,
                                "leechers": leechers,
                                "category": category,
                                "uploader": uploader,
                                "imdb_id": imdb_url.split("=")[-1],
                                "hash": re.search(
                                    r"([{a-f\d,A-F\d}]{32,40})\b", magnet
                                ).group(0),
                                "magnet": magnet,
                                "torrent": torrent,
                                "url": self.BASE_URL + url,
                                "date": date,
                            }
                        )
                    if len(my_dict["data"]) == self.LIMIT:
                        break
                try:
                    ul = soup.find_all("ul", class_="pagination")[-1]
                    tpages = ul.find_all("li")[-2]
                    my_dict["current_page"] = int(
                        soup.select_one("li.page-item.active.txlight a").text.split(
                            " "
                        )[0]
                    )
                    my_dict["total_pages"] = int(tpages.find("a").text)
                except:
                    my_dict["current_page"] = None
                    my_dict["total_pages"] = None
                    # ...
                return my_dict
        except:
            return None

    async def search(self, query, page, limit):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            self.LIMIT = limit
            url = (
                self.BASE_URL
                + "/torrents.php?search=+{}&sort=seeders&order=desc&page={}".format(
                    query, page - 1
                )
            )
            return await self.parser_result(start_time, url, session)

    async def get_torrent_by_url(self, torrent_url):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            return await self.parser_result(
                start_time, torrent_url, session, is_individual=True
            )

    async def parser_result(self, start_time, url, session, is_individual=False):
        html = await Scraper().get_all_results(session, url)
        if is_individual:
            results = self._parser_individual(html)
        else:
            results = self._parser(html)
        if results is not None:
            results["time"] = time.time() - start_time
            results["total"] = len(results["data"])
            return results
        return results

    async def trending(self, category, page, limit):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            self.LIMIT = limit
            url = self.BASE_URL
            return await self.parser_result(start_time, url, session)

    async def recent(self, category, page, limit):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            self.LIMIT = limit
            if not category:
                url = self.BASE_URL + "/latest"
            else:
                if category == "documentaries":
                    category = "Docus"
                url = (
                    self.BASE_URL
                    + "/torrents.php?parent_cat={}&sort=id&order=desc&page={}".format(
                        str(category).capitalize(), page - 1
                    )
                )
            return await self.parser_result(start_time, url, session)

    #! Maybe Implemented in Future
