from random import choice
import requests
from bs4 import BeautifulSoup
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
    proxy = {'https': choosen_proxy}
    return proxy

def check_proxy(url, **kwargs):
    while True:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.get(url, proxies = proxy, timeout = 7, **kwargs)
            print(response.status_code)
            print(response.text)
            proxy['https'] = f"https://{proxy['https']}"
            return proxy
            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass

        # Sleep a random number of seconds (between 1 and 5)
        sleep(randint(1, 5))


valid_proxy = check_proxy("https://httpbin.org/ip")
print(valid_proxy)


def data_scraper(url_scrap):
    # add user_agent
    ua = UserAgent()
    headers = {"user-agent": ua.random}

    # fetch the html page with a http get request
    response = requests.get(url_scrap, headers = headers, proxies = valid_proxy)
    # proxies = valid_proxy

    # parse the html content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    print(response.status_code)


data_scraper("https://amazon.eg")
