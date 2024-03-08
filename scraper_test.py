from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.noon.com/egypt-en/search/?q=smart%20watch&page=3")
# sc-5c17cc27-0 eCGMdH wrapper productContainer
get_source = driver.page_source
product = driver.find_element(By.CSS_SELECTOR, 'span.productContainer')
images = product.find_elements(By.CSS_SELECTOR, 'img')
for image in images:
    print(image.get_attribute('src'))

# nb_products = len(products)
# print(nb_products)

# products_text = []
# for product in products:
#     products_text.append(product.text.split("\n"))
rating = driver.find_element(By.CSS_SELECTOR, 'div.sc-363ddf4f-2')
price = driver.find_element(By.CSS_SELECTOR, 'strong.amount')


# driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
# product_information : <div class="sc-901298d2-0 iWdiZf grid">
# image_url and description : <div class="sc-d8caf424-2 fJBKzl"><img src="https://f.nooncdn.com/p/pnsku/N70033897V/45/_/1708604497/a25a0310-829a-4f3d-b0b1-7d23f03c7981.jpg?format=avif&amp;width=240" alt="Oraimo Watch 4 Plus Bluetooth Call Smart Watch 2.01inch HD Display Fitness Tracker with Heart Rate Sleep Monitor Pedometer IP68 Waterproof Black " width="100%" height="100%" class="sc-19edbe5f-1 fvGuCn"></div>
# color : use the color list and the description
# brand : use the brand list and the description
# rating <div class="sc-363ddf4f-2 jdbOPo">5.0</div>
# price <div class="sc-8df39a2e-1 hCDaLm"><span class="currency">EGP </span><strong class="amount">1,400</strong></div>
# add new colors and brands to the lists