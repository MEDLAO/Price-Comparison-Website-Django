from scraper.websites.utils import *
from scraper.websites.amazon import fetch_amazon, NB_PAGES_AMAZON_EG
from scraper.websites.noon import fetch_noon, NB_PAGES_NOON_EG
import aiohttp as aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


async def fetch_btech(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            async with s.get(f"https://btech.com/en/catalogsearch/result/?q=smart%20watches", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                print(soup.prettify())

        except aiohttp.ClientError:
            await asyncio.sleep(1)


async def main():
    urls = range(1, 2)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls, fetch_btech)
        return htmls

asyncio.run(main())
