from scraper.websites.utils import *
import requests
from bs4 import BeautifulSoup


def twob_scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    products = soup.find_all("li", class_="item product product-item")
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

        image_with_html_tag =  product.find("img", class_="product-image-photo")
        if image_with_html_tag:
            image = image_with_html_tag.attrs['data-src']
            print(image)
        # link
        link_with_html_tag = product.find("a")
        if link_with_html_tag:
            link = link_with_html_tag.attrs['href']
            print(link)

    # print(response.text)
    print(len(products))

twob_scrape(f"https://2b.com.eg/en/accessories/wearables/smart-watch.html")
