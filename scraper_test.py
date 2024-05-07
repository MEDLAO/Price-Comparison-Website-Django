from scraper.websites.utils import *
import requests
from bs4 import BeautifulSoup


def ehabgroup_scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    products = soup.find_all("div", class_="product-item-info")
    for product in products:
        a_links = product.find_all("a")

        # price
        price_with_html_tag = product.find("span", class_="price")
        if price_with_html_tag:
            price = price_with_html_tag.get_text()
            print(price)

        # description
        description = a_links[1].get_text()
        print(description)

        # brand
        brand = find_product_attribute(BRANDS_EN, description)
        print(brand)

        # color
        color = find_product_attribute(COLORS_EN, description)
        print(color)

        # image
        image_with_html_tag =  product.find("img", class_="product-image-photo hover_image")
        if image_with_html_tag:
            image = image_with_html_tag.attrs['src']
            print(image)

        # link
        link = a_links[0].attrs['href']
        print(link)

    # print(len(products))
    # print(products)
    # print(response.text)

ehabgroup_scrape(f"https://ehabgroup.com/smart-wearables/smart-watches.html")
