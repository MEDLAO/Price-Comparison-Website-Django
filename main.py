from scraper.websites.utils import *
from scraper.websites.amazon import fetch_amazon, NB_PAGES_AMAZON_EG
from scraper.websites.twob import fetch_twob
from scraper.websites.jumia import fetch_jumia
from scraper.websites.ehabgroup import fetch_ehabgroup
import aiohttp as aiohttp
import csv
import os


async def main():
    urls = range(1, 3)
    file_path = 'scraper/products-ar.csv'
    # define the header
    field_names = ['website', 'description', 'brand', 'color', 'price', 'currency', 'product_url', 'image_url']

    # Check if the file exists and write headers if it doesn't
    if not os.path.isfile(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(field_names)

    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls, fetch_ehabgroup, file_path)
        return htmls

asyncio.run(main())
