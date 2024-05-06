from scraper.websites.utils import *
import requests
from bs4 import BeautifulSoup


def jumia_scrape(url):
    # headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    products = soup.find_all("article", class_="prd _fb col c-prd")
    for product in products:
        # price
        price_with_html_tag = product.find("div", class_="prc")
        if price_with_html_tag:
            price = price_with_html_tag.get_text()
            print(price)

        # description
        description = product.find("h3", class_="name").get_text()
        print(description)

        # brand
        brand = find_product_attribute(BRANDS_EN, description)
        print(brand)

        # color
        color = find_product_attribute(COLORS_EN, description)
        print(color)

        # image
        image_with_html_tag =  product.find("img", class_="img")
        if image_with_html_tag:
            image = image_with_html_tag.attrs['data-src']
            print(image)

        # link
        link_with_html_tag = product.find("a", class_="core")
        if link_with_html_tag:
            link = link_with_html_tag.attrs['href']
            final_link = "https://www.jumia.com.eg/" + link
            print(final_link)

    print(len(products))
    # print(response.text)

jumia_scrape(f"https://www.jumia.com.eg/catalog/?q=smart+watches")
