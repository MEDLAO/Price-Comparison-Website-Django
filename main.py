import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from io import StringIO
import random


amazon_product_url_ar = "https://www.amazon.eg/s?k=smart+watch&language=ar_AE&crid=VEA91KM5TLZU&" \
                        "sprefix=%2Caps%2C158&ref=nb_sb_ss_recent_1_0_recent"
amazon_product_url_en = "https://www.amazon.eg/s?k=smart+watch&language=en_AE&crid=VEA91KM5TLZU&" \
                        "sprefix=%2Caps%2C158&ref=nb_sb_ss_recent_1_0_recent"

# # Rotating user-agents
# user_agent_list = [
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
# ]
#
# random_user_agent = random.choice(user_agent_list)
#
# # populate headers
# headers = {"user-agent":random_user_agent,
#            #"Accept-Language": "ar-ae,en-ae"
#            }
#
# # Rotating proxies
#
# # parse the free proxies form the HTML
# proxy_list = []
# response = requests.get('https://free-proxy-list.net/')
# df = pd.read_html(StringIO(str(response.text)))[0]
# for ip, port in zip(df['IP Address'], df['Port']):
#     proxy_list.append(ip + ':' + str(port))
# print(proxy_list)
#
# working_proxies = []
# for i in proxy_list[:5]:
#     try:
#         proxy = {'http':'http://' + i,
#                  'https':'https://' + i}
#         res = requests.get('http://example.org/', proxies = proxy)
#         working_proxies.append(proxy)
#     except:
#         pass
#
# print(working_proxies)


# Fetching data and cleaning it
random_proxy = random.choice(working_proxies)
page = requests.get(url=amazon_product_url_ar, headers=headers, proxies = random_proxy)
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
