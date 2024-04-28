from utils import *
import asyncio
from pyppeteer import launch
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
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
    content = await page.content()
    products = await page.querySelectorAll('.productContainer')
    await browser.close()
    print(products)

asyncio.run(noon_scrape('https://www.noon.com/egypt-en/search/?q=smart+20watch'))

    # content = await page.content()
    # price
    # description
    # brand
    # color
    # image
    # link
