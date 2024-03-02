from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import asyncio
import aiohttp as aiohttp
import re
from utils import BRANDS_EN, BRANDS_AR


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


