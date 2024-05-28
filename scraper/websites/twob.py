from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp


HOME_PAGE_URL_TWOB = "https://2b.com.eg/en/"
TWOB_PRODUCT_URL_AR = "https://2b.com.eg/ar/mobile-and-tablet/wearables.html"
TWOB_PRODUCT_URL_EN = "https://2b.com.eg/en/mobile-and-tablet/wearables.html"


async def fetch_twob(s, url, headers):
    data = None
    while data is None:
        try:
            async with s.get(f"https://2b.com.eg/en/mobile-and-tablet/wearables.html?p={url}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all("li", class_="item product product-item")
                print(f'Product for page {url}')
                for product in products:

                    # price
                    price_with_html_tag = product.find("span", class_="price")
                    if price_with_html_tag:
                        price = price_with_html_tag.get_text()
                        price = re.sub(r'جنيه|EGP', '', price)
                        price = re.sub(r'[\s\u00A0\u200f]+', '', price)
                        price = re.sub(r',', '', price).strip()
                        price = float(price)
                        print(price)

                    # description
                    description = product.find("a", class_="product-item-link").get_text().lstrip()
                    print(description)

                    # brand, color
                    brand, color = extract_brand_and_color(description, BRANDS_EN, COLORS_EN)
                    print(brand)
                    print(color)

                    # image
                    image_with_html_tag = product.find("img", class_="product-image-photo")
                    if image_with_html_tag:
                        image = image_with_html_tag.attrs['data-src']
                        print(image)

                    # link
                    link_with_html_tag = product.find("a")
                    if link_with_html_tag:
                        link = link_with_html_tag.attrs['href']
                        print(link)
                print(headers)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
