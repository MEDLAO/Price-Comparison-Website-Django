import asyncio
import aiohttp as aiohttp
from random import choice
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from fake_useragent import UserAgent
import re


HOME_URL = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"
NB_PROXIES_ALTERNATE = 20
NB_PAGES_AMAZON_EG = 37
NB_TRIES_SAME_PAGE = 10
BRANDS_EN = ["Oraimo", "Xiaomi", "HUAWEI", "Joyroom", "SAMSUNG", "Honor", "Amazfit", "JOYROOM", "Apple"]
COLORS_EN = ["Beige", "Black", "Blue", "Brown", "Gold", "Green", "Grey", "Off-White", "Orange", "Pink", "Purple", "Red", "Silver", "Turquoise", "White", "Yellow"]

BRANDS_AR = ["اورايمو", "شاومي", "هواوى" , "جوي رووم", "سامسونج", "اونر", "امازفيت", "جوي رووم", "ابل"]
COLORS_AR = ["بيج", "أسود", "أزرق", "بني","ذهبي", "متعدد", "أوف ويت", "برتقالي", "زهري", "بنفسجي", "أحمر", "فضي", "فبروزي", "أبيض" ,"أصفر", "أخضر" ,"رمادي"]

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
                for product in products[0]:
                    # price
                    price_with_html_tag = product.find('span', class_='a-offscreen')
                    if price_with_html_tag:
                        price = price_with_html_tag.get_text()
                        price = re.sub(r'جنيه', '', price)
                        print(price)

                    # description
                    description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                                                                            'a-text-normal')
                    if description_with_html_tag:
                        description = description_with_html_tag.get_text()
                        print(description)

                        #brand
                        for brand in BRANDS_EN:
                            if (brand in description) or (brand.lower() in description) or (brand.upper() in description):
                                print(brand)
                                break


                        #color
                        for color in COLORS_EN:
                            if (color in description) or (color.lower() in description) or (color.upper() in description):
                                print(color)
                                break


                    # image
                    image_with_html_tag = product.find('img', class_='s-image')
                    if image_with_html_tag:
                        image = image_with_html_tag.attrs['src']
                        print(image)

                    # link
                    link_with_html_tag = product.find('a', class_='a-link-normal s-no-outline')
                    if link_with_html_tag:
                        link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
                        print(link)

        except aiohttp.ClientError:
            await asyncio.sleep(1)


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
