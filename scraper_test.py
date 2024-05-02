from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper.websites.utils import *
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import re
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp as aiohttp
from pyppeteer import launch

def ehabgroup_scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    images = soup.find_all("img", class_="product-image-photo default_image porto-lazyload porto-lazyload-loaded")
    # print(response.text)
    print(len(images))

ehabgroup_scrape(f"https://2b.com.eg/en/accessories/wearables/smart-watch.html")

# <img class="product-image-photo default_image porto-lazyload porto-lazyload-loaded"