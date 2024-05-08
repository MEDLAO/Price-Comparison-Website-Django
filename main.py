from scraper.websites.utils import *
from scraper.websites.amazon import fetch_amazon, NB_PAGES_AMAZON_EG
from scraper.websites.twob import fetch_twob
from scraper.websites.jumia import fetch_jumia
from scraper.websites.ehabgroup import fetch_ehabgroup
import aiohttp as aiohttp


async def main():
    urls = range(1, 3)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls, fetch_ehabgroup)
        return htmls

asyncio.run(main())
