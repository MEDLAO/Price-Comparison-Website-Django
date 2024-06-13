from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp
import aiofiles
import asyncio
import csv
import convert_numbers


HOME_PAGE_URL_EHABGROUP = "https://ehabgroup.com/"
EHABGROUP_URL_AR = "https://ehabgroup.com/ar/smart-wearables.html"
EHABGROUP_URL_EN = "https://ehabgroup.com/smart-wearables.html"
NB_PAGES_EHABGROUP_EG = 2


async def fetch_ehabgroup(s, url, nb_page, headers, file_path, brand_list, color_list, currency):
    data = None
    while data is None:
        try:
            async with s.get(url + f"?p={nb_page}", headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all("div", class_="product-item-info")
                print(f'Product for page {nb_page}')
                for product in products:
                    # initialize default values
                    price = None
                    description = None
                    brand = None
                    color = None
                    link = None
                    image = None

                    description_with_html_tag = product.find("a", class_="product-item-link")
                    if description_with_html_tag:
                        a_links = product.find_all("a")

                        # price
                        price_with_html_tag = product.find("span", class_="price")
                        if price_with_html_tag:
                            price_with_currency = price_with_html_tag.get_text()
                            price = re.sub(r'ج.م|EGP', '', price_with_currency)
                            price = re.sub(r'[\s\u00A0\u200f]+', '', price)
                            price = re.sub(r',', '', price).strip()
                            if 'ج.م' in price_with_currency:
                                price = convert_arabic_price(price)
                            print(price)

                        # description
                        description = description_with_html_tag.get_text()
                        description = description.lstrip().rstrip()
                        print(description)

                        # brand, color
                        brand, color = extract_brand_and_color(description, brand_list, color_list)
                        print(brand)
                        print(color)

                        # image
                        image_with_html_tag = product.find("img", class_="product-image-photo")
                        if image_with_html_tag:
                            image = image_with_html_tag.attrs['data-src']
                            print(image)

                        # link
                        link = a_links[0].attrs['href']
                        print(link)

                        # create product dictionary
                        product_data = [description, brand, color, price, currency, link, image]

                        # write product data to the CSV file asynchronously
                        async with aiofiles.open(file_path, mode='a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            await writer.writerow(product_data)

                print(headers)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
