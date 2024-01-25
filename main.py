import requests
from bs4 import BeautifulSoup
import re
from requests_ip_rotator import ApiGateway
import os
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ACCESS_KEY_SECRET')

api_url = "https://sbvb9w3uj7.execute-api.us-west-2.amazonaws.com"
amazon_product_url_ar = api_url + "/s?k=smart+watch&language=ar"
amazon_product_url_en = api_url + "/s?k=smart+watch&language=en"


# Create gateway object and initialise in
# AWS API Gateway's large IP pool as a proxy to generate pseudo-infinite IPs
gateway = ApiGateway(api_url, access_key_id = AWS_ACCESS_KEY_ID, access_key_secret = ACCESS_KEY_SECRET)
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount(api_url, gateway)

# Send request (IP will be randomised)
response = session.get(amazon_product_url_en)
print(response.status_code)

# Fetching data and cleaning it
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())

products = soup.find_all('div', class_='a-section a-spacing-base')

for product in products:
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

# Pagination


# Delete gateways
gateway.shutdown()
