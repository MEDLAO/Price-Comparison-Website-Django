import requests
from bs4 import BeautifulSoup
import re
from requests_ip_rotator import ApiGateway
import os
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ACCESS_KEY_SECRET')

api_url = "https://amazon.eg"
amazon_product_url_ar = api_url + "/s?k=smart+watch&crid=2VO6ZUHG1QLMC&sprefix=smart%2Caps%2C149&ref=nb_sb_ss_ts-doa-p_1_5"
amazon_product_url_en = api_url + "/s?k=smart+watch&language=en"


# Create gateway object and initialise in
# AWS API Gateway's large IP pool as a proxy to generate pseudo-infinite IPs
gateway = ApiGateway(api_url, access_key_id = AWS_ACCESS_KEY_ID, access_key_secret = ACCESS_KEY_SECRET)
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount(api_url, gateway)

url = api_url

# Send request (IP will be randomised)
response = session.get(url)
print(response.status_code)

# Fetching data and cleaning it
soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify())

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

    # next_button_with_html_tags = soup.div('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator')
    # next_button = next_button_with_html_tags[0].attrs['href']

# Delete gateways
gateway.shutdown()

# 3rd approach : use selenium to search 'smart watch' in the search bar.