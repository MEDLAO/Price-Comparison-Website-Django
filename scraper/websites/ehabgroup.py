from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp


HOME_PAGE_URL_BTECH = "https://btech.com/en/"
BTECH_PRODUCT_URL_AR = "https://btech.com/ar/catalogsearch/result/index/?q=smart+watches"
BTECH_PRODUCT_URL_EN = "https://btech.com/en/catalogsearch/result/?q=smart%20watches"
# NB_PAGES_BTECH_EG =


async def fetch_ehabgroup(s, url, headers):
    data = None
    while data is None:
        try:
            async with s.get(f"https://ehabgroup.com/smart-wearables/smart-watches.html?p={url}", headers=headers) as r:
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
                            print(price)

                        # description
                        description = description_with_html_tag.get_text()
                        print(description)

                        # brand
                        brand = find_product_attribute(BRANDS_EN, description)
                        print(brand)

                        # color
                        color = find_product_attribute(COLORS_EN, description)
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
                print(headers)

        except aiohttp.ClientError:
            await asyncio.sleep(1)
