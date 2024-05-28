from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
import re


HOME_PAGE_URL_AMAZON = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"
NB_PAGES_AMAZON_EG = 37


async def fetch_amazon(s, url, headers):
    data = None
    while data is None:
        try:
            async with s.get(f"https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&page={url}&language=ar_AE&ref=lp_21832958031_sar", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all('div', class_='a-section a-spacing-base')
                print(f'Product for page {url}')
                for product in products:
                    # price
                    price_with_html_tag = product.find('span', class_='a-offscreen')
                    if price_with_html_tag:
                        price = price_with_html_tag.get_text()
                        price = re.sub(r'جنيه|EGP', '', price)
                        price = re.sub(r'[\s\u00A0\u200f]+', '', price)
                        price = re.sub(r',', '', price).strip()
                        price = float(price)
                        print(price)

                    # description
                    description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                                                                            'a-text-normal')
                    if description_with_html_tag:
                        description = description_with_html_tag.get_text()
                        print(description)

                        # brand, color
                        brand, color = extract_brand_and_color(description, BRANDS_AR, COLORS_AR)
                        print(brand)
                        print(color)

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
                print(headers)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
