import requests
from bs4 import BeautifulSoup
import re


amazon_product_url = "https://www.amazon.eg/s?k=smart+watch&ref=nb_sb_noss"

# populate headers
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                        " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# Fetching data and cleaning it
page = requests.get(url=amazon_product_url, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
#print(soup.prettify())

products = soup.find_all('div', class_='a-section a-spacing-base')

for product in products:

    # brand

    # class ="a-size-mini s-line-clamp-1" > < span class ="a-size-base-plus a-color-base" > KOSPET < / span > < / h2 >
    h2 = product.find('h2', class_='a-size-mini s-line-clamp-1')
    print(h2)

    # brand = h2.find_all('span')
    # print(brand)

    # price
    price_with_html_tag = product.find('span', class_='a-offscreen')
    if price_with_html_tag:
        price = price_with_html_tag.get_text()
        price = re.sub(r'جنيه', '', price)
        print(price)

    # description
    description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                                                        'a-text-normal')
    description = description_with_html_tag.get_text()
    print(description)

    # image
    image_with_html_tag = product.find('img', class_='s-image')
    image = image_with_html_tag.attrs['src']
    print(image)

    # link
    link_with_html_tag = product.find('a', class_='a-link-normal s-no-outline')
    link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
    print(link)
