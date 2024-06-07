from scraper.websites.utils import *
from scraper.websites.amazon import *
from scraper.websites.twob import *
from scraper.websites.jumia import *
from scraper.websites.ehabgroup import *
import aiohttp as aiohttp
import csv
import os


async def main():
    file_paths = ['scraper/products-ar.csv']

    data = {
        # 'en': {
        #     'urls': [AMAZON_PRODUCT_URL_EN, JUMIA_PRODUCT_URL_EN, EHABGROUP_URL_EN, TWOB_PRODUCT_URL_EN],
        #     'brands': BRANDS_EN,
        #     'colors': COLORS_EN,
        #     'currency': 'EGP'
        # },
        'ar': {
            'urls': [AMAZON_PRODUCT_URL_AR, JUMIA_PRODUCT_URL_AR, EHABGROUP_URL_AR, TWOB_PRODUCT_URL_AR],
            'brands': BRANDS_AR,
            'colors': COLORS_AR,
            'currency': 'ج.م'
        },
    }

    function_list = [fetch_amazon, fetch_jumia, fetch_ehabgroup, fetch_twob]

    last_pages = [NB_PAGES_AMAZON_EG, NB_PAGES_JUMIA_EG, NB_PAGES_EHABGROUP_EG, NB_PAGES_2B_EG]

    # define the header
    field_names = ['description', 'brand', 'color', 'price', 'currency', 'product_url', 'image_url']

    tasks = []

    for lang, file_path in zip(['ar'], file_paths):
        urls = data[lang]['urls']
        brands = data[lang]['brands']
        colors = data[lang]['colors']
        currency = data[lang]['currency']
        for function, url, last_page in zip(function_list, urls, last_pages):
            # Check if the file exists and write headers if it doesn't
            if not os.path.isfile(file_path):
                with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(field_names)

            async with aiohttp.ClientSession() as session:
                task = await fetch_alls(session, url, last_page, function, file_path, brands, colors, currency)
                tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())
