import os
import asyncio
from .asyncioPoliciesFix import decorator_asyncio_fix
from constants.headers import HEADER_AIO

HTTP_PROXY = os.environ.get("HTTP_PROXY", None)


class Scraper:
    @decorator_asyncio_fix
    async def _get_html(self, session, url):
        try:
            async with session.get(url, headers=HEADER_AIO, proxy=HTTP_PROXY) as r:
                return await r.text()
        except:
            return None

    async def get_all_results(self, session, url):
        return await asyncio.gather(asyncio.create_task(self._get_html(session, url)))
