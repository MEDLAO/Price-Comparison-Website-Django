from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp


async def fetch_twob(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            async with s.get(f"https://2b.com.eg/en/accessories/wearables/smart-watch.html?p={url}", headers=headers) as r:
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
                        print(price)
                    # description
                    description = product.find("a", class_="product-item-link").get_text().lstrip()
                    print(description)
                    # brand
                    brand = find_product_attribute(BRANDS_EN, description)
                    print(brand)
                    # color
                    color = find_product_attribute(COLORS_EN, description)
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

        except aiohttp.ClientError:
            await asyncio.sleep(1)