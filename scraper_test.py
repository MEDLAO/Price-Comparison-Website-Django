from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.amazon.eg/")

get_source = driver.page_source
# products = driver.find_elements(By.CSS_SELECTOR, 'span.productContainer')
# products = driver.find_element(By.CLASS_NAME, 'sc-5c17cc27-0 eCGMdH wrapper productContainer')
# products_text = []
# for product in products:
#     products_text.append(product.text)
print(get_source.text)
