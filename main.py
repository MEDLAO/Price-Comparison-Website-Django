import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from io import StringIO


amazon_product_url_ar = "https://www.amazon.eg/s?k=smart+watch&language=ar_AE&crid=VEA91KM5TLZU&" \
                        "sprefix=%2Caps%2C158&ref=nb_sb_ss_recent_1_0_recent"
amazon_product_url_en = "https://www.amazon.eg/s?k=smart+watch&language=en_AE&crid=VEA91KM5TLZU&" \
                        "sprefix=%2Caps%2C158&ref=nb_sb_ss_recent_1_0_recent"

# populate headers
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                        " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
           #"Accept-Language": "ar-ae,en-ae"
           }

# Rotating proxies

# parse the free proxies form the HTML
prox_list = []
response = requests.get('https://free-proxy-list.net/')
df = pd.read_html(StringIO(str(response.text)))[0]
for ip, port in zip(df['IP Address'], df['Port']):
    prox_list.append(ip + ':' + str(port))
print(prox_list)

# Fetching data and cleaning it
page = requests.get(url=amazon_product_url_ar, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
#print(soup.prettify())

products = soup.find_all('div', class_='a-section a-spacing-base')

for product in products:
    # price
    price_with_html_tag = product.find('span', class_='a-offscreen')
    if price_with_html_tag:
        price = price_with_html_tag.get_text()
        price = re.sub(r'جنيه', '', price)
        #print(price)

    # description
    description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                                                        'a-text-normal')
    description = description_with_html_tag.get_text()
    #print(description)

    # image
    image_with_html_tag = product.find('img', class_='s-image')
    image = image_with_html_tag.attrs['src']
    #print(image)

    # link
    link_with_html_tag = product.find('a', class_='a-link-normal s-no-outline')
    link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
    #print(link)
