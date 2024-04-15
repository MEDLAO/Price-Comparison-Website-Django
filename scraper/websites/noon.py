from utils import *
import asyncio
from pyppeteer import launch
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
from selenium import webdriver
from selenium.webdriver.common.by import By


HOME_PAGE_URL_NOON = "https://www.noon.com/egypt-en/"
NOON_PRODUCT_URL_AR = "https://www.noon.com/egypt-ar/search/?q=smart%20watch"
NOON_PRODUCT_URL_EN = "https://www.noon.com/egypt-en/search/?q=smart%20watch"
NB_PAGES_NOON_EG = 14


async def noon_scrape(url):
    # create a user_agent object
    ua = UserAgent()
    browser = await launch()
    page = await browser.newPage()
    user_agent = ua.random
    await page.setUserAgent(user_agent)
    await page.goto(url)
    # content = await page.content()
    products = await page.querySelectorAll(".sc-424bebc3-0.dvQhRS")
    first_product = products[0]
    fp_txt = await page.evaluate('(first_product) => first_product.innerText', first_product)
    await browser.close()
    return first_product

async def main_noon_jumia():
    fp_text = await noon_scrape('https://www.noon.com/egypt-en/search/?q=smart%20watch')
    print(fp_text)

asyncio.run(main_noon_jumia())

"""async def fetch_noon(s, url):
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
"""

