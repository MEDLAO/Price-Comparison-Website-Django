from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp


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
            async with s.get(f"https://www.noon.com/egypt-en/search/?q=smart%20watch&page={url}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                # products = soup.find_all('div', class_='sc-901298d2-0 iWdiZf grid')
                # print(f'Product for page {url}')
                # print(products)
                # for product in products[0]:
                #     # price
                #     price_with_html_tag = product.find('span', class_='a-offscreen')
                #     if price_with_html_tag:
                #         price = price_with_html_tag.get_text()
                #         price = re.sub(r'جنيه', '', price)
                #         print(price)
                #
                #     # description
                #     description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                #                                                             'a-text-normal')
                #     if description_with_html_tag:
                #         description = description_with_html_tag.get_text()
                #         print(description)
                #
                #         #brand
                #         for brand in BRANDS_EN:
                #             if (brand in description) or (brand.lower() in description) or (brand.upper() in description):
                #                 print(brand)
                #                 break
                #
                #
                #         #color
                #         for color in COLORS_EN:
                #             if (color in description) or (color.lower() in description) or (color.upper() in description):
                #                 print(color)
                #                 break
                #
                #
                #     # image
                #     image_with_html_tag = product.find('img', class_='s-image')
                #     if image_with_html_tag:
                #         image = image_with_html_tag.attrs['src']
                #         print(image)
                #
                #     # link
                #     link_with_html_tag = product.find('a', class_='a-link-normal s-no-outline')
                #     if link_with_html_tag:
                #         link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
                #         print(link)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
