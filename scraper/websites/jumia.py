from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
import aiofiles
import asyncio
import csv


HOME_PAGE_URL_JUMIA = "https://www.jumia.com.eg/"
JUMIA_PRODUCT_URL_AR = "https://www.jumia.com.eg/ar/catalog/?q=smart+watches"
JUMIA_PRODUCT_URL_EN = "https://www.jumia.com.eg/catalog/?q=smart+watches"
NB_PAGES_JUMIA_EG = 50


async def fetch_jumia(s, url, nb_page, headers, file_path, brand_list, color_list, currency):
    data = None
    while data is None:
        try:
            async with s.get(url + f"&page={nb_page}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all("article", class_="prd _fb col c-prd")
                print(f'Product for page {nb_page}')
                for product in products:
                    # initialize default values
                    price = None
                    description = None
                    brand = None
                    color = None
                    final_link = None
                    image = None

                    # price
                    price_with_html_tag = product.find("div", class_="prc")
                    if price_with_html_tag:
                        price = price_with_html_tag.get_text()
                        price = re.sub(r'جنيه|EGP', '', price)
                        price = re.sub(r'[\s\u00A0\u200f]+', '', price)
                        price = re.sub(r',', '', price).strip()
                        print(price)

                    # description
                    description = product.find("h3", class_="name").get_text()
                    print(description)

                    # brand, color
                    brand, color = extract_brand_and_color(description, brand_list, color_list)
                    print(brand)
                    print(color)

                    # image
                    image_with_html_tag = product.find("img", class_="img")
                    if image_with_html_tag:
                        image = image_with_html_tag.attrs['data-src']
                        print(image)

                    # link
                    link_with_html_tag = product.find("a", class_="core")
                    if link_with_html_tag:
                        link = link_with_html_tag.attrs['href']
                        final_link = "https://www.jumia.com.eg/" + link
                        print(final_link)

                        # create product dictionary
                        product_data = [description, brand, color, price, currency, final_link, image]

                        # write product data to the CSV file asynchronously
                        async with aiofiles.open(file_path, mode='a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            await writer.writerow(product_data)

                print(headers)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
