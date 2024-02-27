import asyncio
import aiohttp as aiohttp
from random import choice
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from fake_useragent import UserAgent


HOME_URL = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"
NB_PROXIES_ALTERNATE = 20
NB_PAGES_AMAZON_EG = 37
NB_TRIES_SAME_PAGE = 10


async def fetch(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            async with s.get(f"https://amazon.eg/-/en/s?i=electronics&bbn=18018102031&rh=n%3A21832958031&fs=true&page={url}&language=en_AE", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all('div', class_='a-section a-spacing-base')
                print(f'Product for page {url}')
                print(products[0])
        except aiohttp.ClientError:
            await asyncio.sleep(1)


                # if r.status == 200:
                #     status_code_wrong = False
                # if r.status != 200:
                #     r.raise_for_status()
                # body = await r.text()
                # soup = BeautifulSoup(body, 'html.parser')
                # products = soup.find_all('div', class_='a-section a-spacing-base')
                # print(f'Product for page {url}')
                # print(products[0])


async def fetch_alls(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res

async def main():
    urls = range(1, 38)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls)
        return htmls


asyncio.run(main())
