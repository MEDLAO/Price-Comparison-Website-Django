import asyncio
import aiohttp as aiohttp
from random import choice
import requests
from bs4 import BeautifulSoup
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

async def fetch(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            async with s.get(f"https://amazon.eg/-/en/s?i=electronics&bbn=18018102031&rh=n%3A21832958031&fs=true&page={url}&language=en_AE", headers=headers) as r:
                r.raise_for_status()
                print(r.status)
                data = await r.text()
                soup = BeautifulSoup(data, 'html.parser')
                products = soup.find_all('div', class_='a-section a-spacing-base')
                print(f'Product for page {url}')
                print(products[0])
        except aiohttp.ClientError:
            await asyncio.sleep(1)

                # if r.status == 200:
                #     status_code_wrong = False
                # if r.status != 200:
                #     r.raise_for_status()
                # body = await r.text()
                # soup = BeautifulSoup(body, 'html.parser')
                # products = soup.find_all('div', class_='a-section a-spacing-base')
                # print(f'Product for page {url}')
                # print(products[0])


async def fetch_alls(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res

async def main():
    urls = range(1, 38)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls)
        return htmls


asyncio.run(main())
