import requests
from bs4 import BeautifulSoup
import re
from requests_ip_rotator import ApiGateway
from fake_useragent import UserAgent


amazon_product_url_ar = "https://www.amazon.eg/s?k=smart+watch&language=ar_AE&crid=VEA91KM5TLZU&" \
                        "sprefix=%2Caps%2C158&ref=nb_sb_ss_recent_1_0_recent"
amazon_product_url_en = "https://www.amazon.eg/s?k=smart+watch&language=en_AE&crid=VEA91KM5TLZU&" \
                        "sprefix=%2Caps%2C158&ref=nb_sb_ss_recent_1_0_recent"

# Rotate User-Agent
ua = UserAgent()
headers = ua.random

# Create gateway object and initialise in
# AWS API Gateway's large IP pool as a proxy to generate pseudo-infinite IPs
gateway = ApiGateway("https://www.amazon.eg/-/en/ref=nav_logo")
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount("https://www.amazon.eg/-/en/ref=nav_logo", gateway)

# Send request (IP will be randomised)
response = session.get(amazon_product_url_en, headers = headers)
print(response.status_code)

# Fetching data and cleaning it
soup = BeautifulSoup(response.content, 'lxml')
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

# Delete gateways
gateway.shutdown()
