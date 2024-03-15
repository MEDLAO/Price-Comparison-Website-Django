from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
import pyppeteer
pyppeteer.chromium_downloader.download_chromium()
from pyppeteer import launch


NOON_PRODUCT_URL_AR = "https://www.noon.com/egypt-ar/search/?q=smart%20watch"
NOON_PRODUCT_URL_EN = "https://www.noon.com/egypt-en/search/?q=smart%20watch"
NB_PAGES_NOON_EG = 16


async def fetch_noon(url):
    browser = await launch({'autoClose': False, })
    # browser = await launch()
    page = await browser.newPage()
    await page.goto(f"https://www.noon.com/egypt-en/search/?q=smart%20watch&page={url}")
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()

async def fetch_alls_noon(urls, fetch_function):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_function(url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res
