from scraper.websites.utils import *
from scraper.websites.amazon import *
from scraper.websites.twob import *
from scraper.websites.jumia import *
from scraper.websites.ehabgroup import *
import aiohttp as aiohttp
import csv
import os


async def main():
    file_paths = ['scraper/products-en.csv', 'scraper/products-ar.csv']
    amazon_urls = [AMAZON_PRODUCT_URL_EN, AMAZON_PRODUCT_URL_AR]
    jumia_urls = [JUMIA_PRODUCT_URL_EN, JUMIA_PRODUCT_URL_AR]
    ehabgroup_urls = [EHABGROUP_URL_EN, EHABGROUP_URL_AR]
    twob_urls = [TWOB_PRODUCT_URL_EN, TWOB_PRODUCT_URL_AR]
    function_list = [fetch_amazon, fetch_jumia, fetch_ehabgroup, fetch_twob]
    last_pages = [NB_PAGES_AMAZON_EG, NB_PAGES_JUMIA_EG, NB_PAGES_EHABGROUP_EG, NB_PAGES_2B_EG]

    # define the header
    field_names = ['website', 'description', 'brand', 'color', 'price', 'currency', 'product_url', 'image_url']

    for last_page, function in zip(last_pages, function_list):
        for file_path, amazon_url, jumia_url, ehabgroup_url, twob_url in zip(file_paths, amazon_urls, jumia_urls, ehabgroup_urls, twob_urls):
            # Check if the file exists and write headers if it doesn't
            if not os.path.isfile(file_path):
                with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(field_names)

            async with aiohttp.ClientSession() as session:
                htmls = await fetch_alls(session, last_page, function, file_path)
                return htmls

asyncio.run(main())
