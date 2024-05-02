from scraper.websites.utils import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp as aiohttp


HOME_PAGE_URL_BTECH = "https://btech.com/en/"
BTECH_PRODUCT_URL_AR = "https://btech.com/ar/catalogsearch/result/index/?q=smart+watches"
BTECH_PRODUCT_URL_EN = "https://btech.com/en/catalogsearch/result/?q=smart%20watches"
# NB_PAGES_BTECH_EG =
