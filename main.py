import requests
from bs4 import BeautifulSoup

amazon_product_url = "https://www.amazon.eg/-/en/?language=en_AE"

# populate headers
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/120.0.0.0 Safari/537.36"}

# Fetching data and cleaning it

page = requests.get(url=amazon_product_url, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
print(soup.prettify())
