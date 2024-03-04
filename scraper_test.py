from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.noon.com/egypt-en/search/?q=smart%20watch&page=2")

get_source = driver.page_source
products = driver.find_elements(By.CSS_SELECTOR, 'span.productContainer')
products_text = []
for product in products:
    products_text.append(product.text)
print(products_text)
