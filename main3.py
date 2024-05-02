import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from scraper.websites.utils import *


HOME_URL = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"
NB_PROXIES_ALTERNATE = 20
NB_PAGES_AMAZON_EG = 37
NB_TRIES_SAME_PAGE = 15


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

