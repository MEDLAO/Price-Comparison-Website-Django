from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp


HOME_PAGE_URL_BTECH = "https://btech.com/en/"
BTECH_PRODUCT_URL_AR = "https://btech.com/ar/catalogsearch/result/index/?q=smart+watches"
BTECH_PRODUCT_URL_EN = "https://btech.com/en/catalogsearch/result/?q=smart%20watches"
# NB_PAGES_BTECH_EG =


async def fetch_btech(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            async with s.get(f"https://btech.com/en/catalogsearch/result/?q=smart%20watches", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                print(soup.prettify())
                # products = soup.find_all('div', class_='a-section a-spacing-base')
                # print(f'Product for page {url}')
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
                #         brand = find_product_attribute(BRANDS_EN, description)
                #         print(brand)
                #         # for brand in BRANDS_EN:
                #         #     if (brand in description) or (brand.lower() in description) or (brand.upper() in description):
                #         #         print(brand)
                #         #         break
                #
                #         #color
                #         color = find_product_attribute(COLORS_EN, description)
                #         print(color)
                #         # for color in COLORS_EN:
                #         #     if (color in description) or (color.lower() in description) or (color.upper() in description):
                #         #         print(color)
                #         #         break
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
