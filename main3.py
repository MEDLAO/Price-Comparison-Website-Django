from random import choice
import requests
from bs4 import BeautifulSoup
import re
from random import randint
from time import sleep
from fake_useragent import UserAgent


response = requests.get("https://sslproxies.org/")

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', class_="table table-striped table-bordered")

ip_addresses = table.find_all('td')[::8]
ports = table.find_all('td')[1::8]

ip_port_tuples = list(zip(map(lambda x:x.text, ip_addresses), map(lambda x:x.text, ports)))
ips_with_ports = list(map(lambda x:x[0]+':'+x[1], ip_port_tuples))
print(ips_with_ports)

def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html.parser')
    choosen_proxy = choice(ips_with_ports)
    proxy = {'http': choosen_proxy}
    return proxy

# create a list altern_list to stock the valid proxies and use the script from the online compiler
def check_proxy(url, **kwargs):
    while True:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.get(url, proxies = proxy, timeout = 7, **kwargs)
            print(response.status_code)
            print(response.text)
            proxy['http'] = f"http://{proxy['http']}"
            return proxy
            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass

        # Sleep a random number of seconds (between 1 and 5)
        sleep(randint(1, 5))

# rotate proxy
valid_proxy = check_proxy("https://httpbin.org/ip")
print(valid_proxy)

home_url = "https://amazon.eg"
amazon_product_url_ar = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
amazon_product_url_en = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"

def data_scraper(url_scrap):
    while True:
        # rotate user_agent
        ua = UserAgent()
        headers = {"user-agent": ua.random}

        # fetch the html page with a http get request
        response = requests.get(url_scrap, headers = headers, proxies = valid_proxy)
        # proxies = valid_proxy

        # parse the html content of the page
        soup = BeautifulSoup(response.content, "lxml")
        # print(soup.prettify())

        products = soup.find_all('div', class_='a-section a-spacing-base')

        for product in products:
            # price
            price_with_html_tag = product.find('span', class_='a-offscreen')
            if price_with_html_tag:
                price = price_with_html_tag.get_text()
                price = re.sub(r'جنيه', '', price)
                # print(price)

            # description
            description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
                                                                    'a-text-normal')
            description = description_with_html_tag.get_text()
            # print(description)

            # image
            image_with_html_tag = product.find('img', class_='s-image')
            image = image_with_html_tag.attrs['src']
            # print(image)

            # link
            link_with_html_tag = product.find('a', class_='a-link-normal s-no-outline')
            link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
            # print(link)

        # next page
        next_page_with_tag = soup.find('a', class_ ="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")

        if not next_page_with_tag:
            break
        next_page = next_page_with_tag.get('href')
        next_page_url = home_url + next_page
        print(next_page_url)
        url_scrap = next_page_url

        sleep(randint(2, 7))


data_scraper(amazon_product_url_en)

