from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
from selenium import webdriver
from selenium.webdriver.common.by import By


NOON_PRODUCT_URL_AR = "https://www.noon.com/egypt-ar/search/?q=smart%20watch"
NOON_PRODUCT_URL_EN = "https://www.noon.com/egypt-en/search/?q=smart%20watch"
NB_PAGES_NOON_EG = 16


async def fetch_noon(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            driver =  await webdriver.Chrome()

            async with s.get(f"https://www.noon.com/egypt-en/search/?q=smart%20watch&page={url}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                # soup = BeautifulSoup(data, 'html.parser')
                # print(soup.prettify())
        except aiohttp.ClientError:
            await asyncio.sleep(1)
