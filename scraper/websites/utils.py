import requests
from bs4 import BeautifulSoup
import asyncio
from random import choice
from time import sleep
from random import randint


NB_PROXIES_ALTERNATE = 20
NB_TRIES_SAME_PAGE = 10

BRANDS_EN = ["Oraimo", "Xiaomi", "HUAWEI", "Joyroom", "SAMSUNG", "Honor", "Amazfit", "Apple", "Tommy Hilfiger", "Diesel", "Fossil", "Casio", "G-shock", "Guess", "Michael Kors", "Barbie"]
COLORS_EN = ["Beige", "Black", "Blue", "Brown", "Gold", "Green", "Grey", "Off-White", "Orange", "Pink", "Purple", "Red", "Silver", "Turquoise", "White", "Yellow"]

BRANDS_AR = ["اورايمو", "شاومي", "هواوى" , "جوي رووم", "سامسونج", "اونر", "امازفيت", "جوي رووم", "ابل", "تومي هيلفيغر", "ديزل", "فوسيل", "كاسيو", "جي شوك", "جس", "مايكل كورس", "باربي"]
COLORS_AR = ["بيج", "أسود", "أزرق", "بني", "ذهبي", "متعدد", "أوف ويت", "برتقالي", "زهري", "بنفسجي", "أحمر", "فضي", "فبروزي", "أبيض" ,"أصفر", "أخضر" ,"رمادي"]


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
    proxy_list = proxy_scraper()
    chosen_proxy = choice(proxy_list)
    proxy = {'http': chosen_proxy}
    return proxy

def check_proxy(url, **kwargs):
    alternating_proxies = []
    count = 0
    while len(alternating_proxies) < NB_PROXIES_ALTERNATE and count < 10:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.get(url, proxies = proxy, **kwargs)
            print(response.status_code)
            print(response.text)
            proxy['http'] = f"http://{proxy['http']}"
            alternating_proxies.append(proxy['http'])
            # sleep(randint(3, 7)) # Sleep a random number of seconds (between 1 and 5)

            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass
        count += 1
    return alternating_proxies

def find_product_attribute(attribute_list, description_text):
    for attribute in attribute_list:
        if ((attribute in description_text) or (attribute.lower() in description_text) or (attribute.upper() in description_text)) and (attribute not in "Bluetooth"):
            return attribute

async def fetch_alls(s, urls, fetch_function):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_function(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res
