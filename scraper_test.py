from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper.websites.utils import *
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import re
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp as aiohttp
from pyppeteer import launch

ua = UserAgent()
headers = {"user-agent": ua.random, 'Authorization': 'Api-Key client-SwdUQtQxWRR0i6jWZ5sfoB5M9v9ZpVEH'}
response = requests.get('https://api.lab.amplitude.com/sdk/vardata', headers=headers)
# data = response.json()
# print(data)
print(response.text)

async def fetch_btech(s, url):
    # create a user_agent object
    ua = UserAgent()
    # rotate user_agent
    headers = {"user-agent": ua.random}

    data = None
    while data is None:
        try:
            async with s.get(url, headers=headers) as r:
                r.raise_for_status()
                data = await r.text()
                print(r.status)
                soup = BeautifulSoup(data, 'html.parser')
                # print(soup.prettify())
                # div = soup.find('div', id='product_view_20')
                # print(div)
                # script = soup.find('script')
                # print(script)
        except aiohttp.ClientError:
            await asyncio.sleep(1)


async def main():
    async with aiohttp.ClientSession() as session:
        await fetch_btech(session, 'https://btech.com/en/catalogsearch/result/?q=smart%20watches')

# asyncio.run(main())


"""async def scrape(url):
    browser = await launch()
    page = await browser.newPage()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    await page.setUserAgent(user_agent)
    await page.goto(url)
    content = await page.content()
    await browser.close()
    return content
# https://www.jumia.com.eg/catalog/?q=smart+watch
async def main():
    content = await scrape('https://www.noon.com/egypt-en/search/?q=smart%20watch')
    print(content)

asyncio.run(main())"""

"""def noon_scrape(url):

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # create a user_agent object
    ua = UserAgent()

    # Get a random User-Agent
    random_user_agent = ua.random
    chrome_options.add_argument(f"--user-agent={random_user_agent}")

    # free proxy server URL
    # valid_proxies = check_proxy("https://httpbin.org/ip")
    # proxy_server_url = choice(valid_proxies)
    # chrome_options.add_argument(f"--proxy-server={proxy_server_url}")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    # use delay function to get all tags
    driver.implicitly_wait(20)
    # sc-5c17cc27-0 eCGMdH wrapper productContainer
    get_source = driver.page_source
    dict_products = {}
    products = driver.find_elements(By.CSS_SELECTOR, 'span.productContainer')
    for product in products[:2]:
        images = product.find_elements(By.CSS_SELECTOR, "img[src^='https://f.nooncdn.com/p/']")
        dict_products["image"] = []
        for image in images:
            # print(image.get_attribute('src'))
            dict_products["image"].append(image.get_attribute('src'))
        link = product.find_element(By.CSS_SELECTOR, "[id^='productBox']").get_attribute('href')  # attribute starts with
        # print(link)
        dict_products["link"] = link
        try:
            rating = product.find_element(By.CSS_SELECTOR, "[class='sc-363ddf4f-2 jdbOPo']").text
        except Exception:
            rating = None
        # print(rating)
        dict_products["rating"] = rating
        price = product.find_element(By.CSS_SELECTOR, 'strong.amount').text
        # print(price)
        dict_products["price"] = price
        description = product.find_element(By.CSS_SELECTOR, "[data-qa^='productImagePLP']").get_attribute('data-qa')
        description = re.sub(r'productImagePLP_', '', description)
        # print(description)
        dict_products["description"] = description
        brand = find_product_attribute(BRANDS_EN, description)
        # print(brand)
        dict_products["brand"] = brand
        color = find_product_attribute(COLORS_EN, description)
        # print(color)
        dict_products["color"] = color
    print(dict_products)

for i in range(1, 15):
    noon_scrape(f"https://www.noon.com/egypt-en/search/?q=smart%20watch&page={i}")"""

# if __name__ == '__main__':
#     urls = [f"https://www.noon.com/egypt-en/search/?q=smart%20watch&page={i}" for i in range(1, 15)]
#     with Pool(4) as p:
#         print(p.map(noon_scrape, urls)

# images = driver.find_elements(By.CSS_SELECTOR, "div img")
# for image in images:
#     print(image.get_attribute('src'))

# links = driver.find_elements(By.CSS_SELECTOR, "[id^='productBox']") # attribute starts with
# for link in links:
#     print(link.get_attribute('href'))
#     print(link.text)

# descriptions = driver.find_elements(By.CSS_SELECTOR, "[data-qa^='productImagePLP']")
# for description in descriptions:
#     print(description.get_attribute('data-qa'))

# nb_products = len(products)
# print(nb_products)

# products_text = []

# rating = driver.find_element(By.CSS_SELECTOR, 'div.sc-363ddf4f-2')
# price = driver.find_element(By.CSS_SELECTOR, 'strong.amount')


# driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
# product_information : <div class="sc-901298d2-0 iWdiZf grid">
# image_url and description : <div class="sc-d8caf424-2 fJBKzl"><img src="https://f.nooncdn.com/p/pnsku/N70033897V/45/_/1708604497/a25a0310-829a-4f3d-b0b1-7d23f03c7981.jpg?format=avif&amp;width=240" alt="Oraimo Watch 4 Plus Bluetooth Call Smart Watch 2.01inch HD Display Fitness Tracker with Heart Rate Sleep Monitor Pedometer IP68 Waterproof Black " width="100%" height="100%" class="sc-19edbe5f-1 fvGuCn"></div>
# color : use the color list and the description
# brand : use the brand list and the description
# rating <div class="sc-363ddf4f-2 jdbOPo">5.0</div>
# price <div class="sc-8df39a2e-1 hCDaLm"><span class="currency">EGP </span><strong class="amount">1,400</strong></div>
# add new colors and brands to the lists

# <img src="https://f.nooncdn.com/p/pzsku/Z3D5583C3993D781D3BE5Z/45/_/1707563204/da956346-b834-48b2-b5f9-056f23e2981e.jpg?format=avif&amp;width=240" alt="W&amp;O X9 Pro 2 (Super AMOLED) Screen Smart Watch (45mm/2.02inch) Screen | Space Aluminum Case , black strap " width="100%" height="100%" class="sc-b2e95a1f-1 ewpZHl">
