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
    images = await url.querySelectorAll("img .sc-d13a0e88-1")
    print(images)
    # html = await page.content()
    # await browser.close()
    # return html

html_response = asyncio.run(noon_scrape('https://www.noon.com/egypt-en/search/?q=smart%20watch'))
# print(html_response)

    # content = await page.content()
    # price
    # description
    # brand
    # color
    # image
    # link

## Load HTML Response into BeautifulSoup
soup = BeautifulSoup(html_response, "html.parser")
# print(soup.prettify())
products = soup.select('div.sc-424bebc3-0.dvQhRS')
# print(products)
for product in products:
    price = product.select_one('strong.amount').get_text()
    # print(price)

    description_with_html_tag = product.select_one('div.sc-b07dc364-24.jyQuMr')
    description = description_with_html_tag.attrs['title']
    # print(description)
    # <div data-qa="product-name" title="Wearfit Pro X8 Ultra MAX Smartwatch Screen 2.2 Inch 485*520 Pixels - Wearfit PRO - Bluetooth V5.2 (Gold) " class="sc-b07dc364-24 jyQuMr">

    image_with_html_tag = product.select_one('img.sc-d13a0e88-1.cindWc')
    # , attrs = {'class': 'sc-d13a0e88-1 cindWc'}
    # attrs={'class': 'card-text p-2'}
    # class_="sc-d13a0e88-1 cindWc"
    # if image_with_html_tag:
        # image = soup.select_one('div.sc-d8caf424-2.fJBKzl')
        # img.sc-d13a0e88-1.cindWc
        # print(image_with_html_tag)
        # images = image_with_html_tag
        # print(product.img)

    # link_with_html_tag = product.find_all("div", id=re.compile("^productBox"))
    # if link_with_html_tag:
    #     link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
    #     # print(link)

divs_img = soup.select('div.lazyload-wrapper')
print(divs_img)

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

