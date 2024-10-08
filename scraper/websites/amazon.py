from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
from urllib.parse import unquote
import re
import aiofiles
import asyncio
import csv


HOME_PAGE_URL_AMAZON = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?i=electronics&rh=n%3A21832878031&fs=true&language=ar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?i=electronics&rh=n%3A21832878031&fs=true&language=en"
NB_PAGES_AMAZON_EG = 400


async def fetch_amazon(s, url, nb_page, headers, file_path, brand_list, color_list, currency):
    """
    Asynchronously fetches product data from Amazon and writes it to a CSV file.
    """
    data = None
    while data is None:
        try:
            async with s.get(url + f"&page={nb_page}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all('div', class_='a-section a-spacing-base')
                print(f'Product for page {nb_page}')
                for product in products:
                    # initialize default values
                    price = None
                    description = None
                    brand = None
                    color = None
                    link = None
                    image = None

                    # price
                    price_with_html_tag = product.find('span', class_='a-offscreen')
                    if price_with_html_tag:
                        price = price_with_html_tag.get_text()
                        price = re.sub(r'جنيه|EGP', '', price)
                        price = re.sub(r'[\s\u00A0\u200f]+', '', price)
                        price = re.sub(r',', '', price).strip()
                        print(price)

                    # description
                    description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                                                                            'a-text-normal')
                    if description_with_html_tag:
                        description = description_with_html_tag.get_text()
                        if '،' in description:
                            description.replace(',', '،')
                        print(description)

                        # brand, color
                        brand, color = extract_brand_and_color(description, brand_list, color_list)
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
                        link = unquote(link)  # decode the url
                        print(link)

                    # create product dictionary
                    product_data = [description, brand, color, price, currency, link, image]
                    product_data = add_latin_letters(product_data)

                    # write product data to the CSV file asynchronously
                    async with aiofiles.open(file_path, mode='a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        await writer.writerow(product_data)

                print(headers)  # ensure there is a user-agent per page

        except aiohttp.ClientError:
            await asyncio.sleep(1)
