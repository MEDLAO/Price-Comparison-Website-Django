from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
import aiofiles
import asyncio
import json
import csv


HOME_PAGE_URL_EHABGROUP = "https://ehabgroup.com/"
EHABGROUP_URL_AR = "https://ehabgroup.com/ar/smart-wearables.html"
EHABGROUP_URL_EN = "https://ehabgroup.com/smart-wearables.html"


async def fetch_ehabgroup(s, url, headers, file_path):
    data = None
    while data is None:
        try:
            async with s.get(f"https://ehabgroup.com/smart-wearables.html?p={url}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all("div", class_="product-item-info")
                print(f'Product for page {url}')
                for product in products:
                    description_with_html_tag = product.find("a", class_="product-item-link")
                    if description_with_html_tag:
                        a_links = product.find_all("a")

                        # price
                        price_with_html_tag = product.find("span", class_="price")
                        if price_with_html_tag:
                            price = price_with_html_tag.get_text()
                            price = re.sub(r'جنيه|EGP', '', price)
                            price = re.sub(r'[\s\u00A0\u200f]+', '', price)
                            price = re.sub(r',', '', price).strip()
                            print(price)

                            currency = 'EGP'
                            print(currency)

                        # description
                        description = description_with_html_tag.get_text()
                        description = description.lstrip()
                        print(description)

                        # brand, color
                        brand, color = extract_brand_and_color(description, BRANDS_EN, COLORS_EN)
                        print(brand)
                        print(color)

                        # image
                        image_with_html_tag = product.find("img",
                                                           class_="product-image-photo hover_image")
                        if image_with_html_tag:
                            image = image_with_html_tag.attrs['src']
                            print(image)

                        # link
                        link = a_links[0].attrs['href']
                        print(link)

                        # create product dictionary
                        product_data = ['Ehab Group', description, brand, color, price, 'EGP', link, image]

                        # Write product data to the CSV file asynchronously
                        async with aiofiles.open(file_path, mode='a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            await writer.writerow(product_data)

                print(headers)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
