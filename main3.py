from random import choice
import requests
from bs4 import BeautifulSoup
import re
from random import randint
from time import sleep
from fake_useragent import UserAgent


HOME_URL = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"
NB_PROXIES_ALTERNATE = 20
NB_PAGES_AMAZON_EG = 37
NB_TRIES_SAME_PAGE = 10


def proxy_scraper():
    response = requests.get("https://sslproxies.org/")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_="table table-striped table-bordered")

    ip_addresses = table.find_all('td')[::8]
    ports = table.find_all('td')[1::8]

    ip_port_tuples = list(zip(map(lambda x:x.text, ip_addresses), map(lambda x:x.text, ports)))
    ips_with_ports = list(map(lambda x:x[0]+':'+x[1], ip_port_tuples))
    return ips_with_ports

def proxy_generator():
    # response = requests.get("https://sslproxies.org/")
    # soup = BeautifulSoup(response.content, 'html.parser')
    proxy_list = proxy_scraper()
    choosen_proxy = choice(proxy_list)
    proxy = {'http': choosen_proxy}
    return proxy

def check_proxy(url, **kwargs):
    alternating_proxies = []
    while len(alternating_proxies) < NB_PROXIES_ALTERNATE:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.get(url, proxies = proxy, **kwargs)
            print(response.status_code)
            print(response.text)
            proxy['http'] = f"http://{proxy['http']}"
            alternating_proxies.append(proxy)
            sleep(randint(3, 7)) # Sleep a random number of seconds (between 1 and 5)

            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass
    return alternating_proxies

def data_scraper(url_scrap):
    # get a list of proxies
    valid_proxies = check_proxy("https://httpbin.org/ip")
    print(valid_proxies)
    # counter_delay = 0
    # create a user_agent object
    ua = UserAgent()
    for i in  range(1, NB_PAGES_AMAZON_EG + 1): # pagination
        # i = 0

        # while True:
        # rotate user_agent
        headers = {"user-agent": ua.random}

        # rotate proxies
        j = i
        valid_proxy = valid_proxies[j % len(valid_proxies)] # we use modulo to start again from the beginning of the list
        print(valid_proxy)
        # i += 1

        # fetch the html page with a http get request
        url_scrap = f"https://amazon.eg/-/en/s?i=electronics&bbn=18018102031&rh=n%3A21832958031&fs=true&page={i}&language=en_AE"

        status_code_wrong = True
        k = 0


        while status_code_wrong and k < NB_TRIES_SAME_PAGE: # retry the request until getting a status code 200
            response = requests.get(url_scrap, headers = headers, proxies = valid_proxy)
            print(f"Status code for page {i} : {response.status_code}")
            sleep(5)
            j += 1 # we try the next proxy
            k += 1
            if response.status_code == 200:
                status_code_wrong = False


        # parse the html content of the page
        soup = BeautifulSoup(response.content, "lxml")
        # print(soup.prettify())

        products = soup.find_all('div', class_='a-section a-spacing-base')
        print(products[0])

        final_products = [] # creating a list of dictionaries
        # for product in products:
        #     final_product = {} # creating a dictionary to store the product information
        #
        #     # price
        #     price_with_html_tag = product.find('span', class_='a-offscreen')
        #     if price_with_html_tag:
        #         price = price_with_html_tag.get_text()
        #         price = re.sub(r'جنيه', '', price)
        #         final_product["price"] = price
        #         # print(price)
        #
        #     # description
        #     description_with_html_tag = product.find('span', class_='a-size-base-plus a-color-base '
        #                                                             'a-text-normal')
        #     description = description_with_html_tag.get_text()
        #     final_product["description"] = description
        #     # print(description)
        #
        #     # image
        #     image_with_html_tag = product.find('img', class_='s-image')
        #     image = image_with_html_tag.attrs['src']
        #     final_product["image"] = image
        #     # print(image)
        #
        #     # link
        #     link_with_html_tag = product.find('a', class_='a-link-normal s-no-outline')
        #     link = "https://www.amazon.eg" + link_with_html_tag.attrs['href']
        #     final_product["link"] = link
        #     # print(link)

        # # next page
        # next_page_with_tag = soup.find('a', class_ ="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")
        #
        # if not next_page_with_tag:
        #     break
        # next_page = next_page_with_tag.get('href')
        # next_page_url = home_url + next_page
        # print(next_page_url)
        # url_scrap = next_page_url

        # counter_delay += 1
        # sleep(randint(20, 60))
        sleep(3)

data_scraper(AMAZON_PRODUCT_URL_EN)
