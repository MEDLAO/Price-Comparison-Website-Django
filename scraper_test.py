from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper.websites.utils import *


driver = webdriver.Chrome()

driver.get("https://www.noon.com/egypt-en/search/?q=smart%20watch&page=5")
# sc-5c17cc27-0 eCGMdH wrapper productContainer
get_source = driver.page_source
products = driver.find_elements(By.CSS_SELECTOR, 'span.productContainer')
for product in products[:3]:
    images = product.find_elements(By.CSS_SELECTOR, "img[src^='https://f.nooncdn.com/p/']")
    for image in images:
        print(image.get_attribute('src'))
    link = product.find_element(By.CSS_SELECTOR, "[id^='productBox']").get_attribute('href')  # attribute starts with
    print(link)
    rating = product.find_element(By.CSS_SELECTOR, "[class='sc-363ddf4f-2 jdbOPo']").text
    print(rating)
    price = product.find_element(By.CSS_SELECTOR, 'strong.amount').text
    print(price)
    description = product.find_element(By.CSS_SELECTOR, "[data-qa^='productImagePLP']").get_attribute('data-qa')
    print(description)
    brand = find_product_attribute(BRANDS_EN, description)
    print(brand)
    color = find_product_attribute(COLORS_EN, description)
    print(color)
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
