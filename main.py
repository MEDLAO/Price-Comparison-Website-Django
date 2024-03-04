from scraper.websites.utils import *
from scraper.websites.amazon import fetch_amazon, NB_PAGES_AMAZON_EG
from scraper.websites.noon import fetch_noon, NB_PAGES_NOON_EG
import aiohttp as aiohttp


async def main():
    urls = range(1, 2)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls, fetch_amazon)
        return htmls

asyncio.run(main())
