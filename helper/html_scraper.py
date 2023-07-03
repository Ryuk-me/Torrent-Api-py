import asyncio
from .asyncioPoliciesFix import decorator_asyncio_fix
from constants.headers import HEADER_AIO

class Scraper:
    @decorator_asyncio_fix
    async def _get_html(self, session, url):
        try:
            async with session.get(
                url,
                headers=HEADER_AIO,
            ) as r:
                return await r.text(encoding="ISO-8859-1")
        except:
            return None

    async def get_all_results(self, session, url):
        return await asyncio.gather(asyncio.create_task(self._get_html(session, url)))
