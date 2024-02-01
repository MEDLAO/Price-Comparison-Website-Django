from random import choice
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep


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
    proxy = {'https': choice(ips_with_ports)}
    return proxy

def check_proxy(url, **kwargs):
    while True:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.get(url, proxies=proxy, timeout=7, **kwargs)
            print(response.status_code)
            print(response.text)
            return proxy
            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass

        # Sleep a random number of seconds (between 1 and 5)
        sleep(randint(1, 5))


valid_proxy = check_proxy("https://httpbin.org/ip")


def data_scraper(url_scrap):
    # add user_agent
    # fetch the html page with a http get request
    response = requests.get(url_scrap, proxies = valid_proxy)

    # parse the html content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    print(response.status_code)


data_scraper("https://amazon.eg")
