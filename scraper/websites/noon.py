from utils import *
import asyncio
from pyppeteer import launch
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
import aiohttp as aiohttp
from selenium import webdriver
from selenium.webdriver.common.by import By


HOME_PAGE_URL_NOON = "https://www.noon.com/egypt-en/"
NOON_PRODUCT_URL_AR = "https://www.noon.com/egypt-ar/search/?q=smart%20watch"
NOON_PRODUCT_URL_EN = "https://www.noon.com/egypt-en/search/?q=smart%20watch"
NB_PAGES_NOON_EG = 14


# async def noon_scrape(url):
#     # create a user_agent object
#     ua = UserAgent()
#     browser = await launch()
#     page = await browser.newPage()
#     user_agent = ua.random
#     await page.setUserAgent(user_agent)
#     await page.goto(url)
#     # content = await page.content()
#     product_images = await page.querySelectorAll('img.sc-d13a0e88-1.cMrpQt')
#     for image in product_images:
#         content = await page.evaluate('(image) => image.innerText', image)
#         print(content)
#     await browser.close()


# asyncio.run(noon_scrape('https://www.noon.com/egypt-en/watch-4-plus-bluetooth-call-smart-watch-2-01inch-hd-display-fitness-tracker-with-heart-rate-sleep-monitor-pedometer-ip68-waterproof-black/N70033897V/p/?o=ca2883ce8758d96e'))


response = requests.get('https://www.noon.com/egypt-en/search/?q=smart%20watch')
html = response.text

# Use Beautiful Soup to parse the HTML
soup = BeautifulSoup(html)
images = soup.find_all(class_='sc-d13a0e88-1 cindWc')
print(images)

    # content = await page.content()
    # price
    # description
    # brand
    # color
    # image
    # link
