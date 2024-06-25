import os
import sys
import django
import pandas as pd
from scraper.websites.utils import normalize_url, truncate, remove_latin_letters, safe_float_conversion
from scraper.websites.amazon import HOME_PAGE_URL_AMAZON
from scraper.websites.jumia import HOME_PAGE_URL_JUMIA
from scraper.websites.ehabgroup import HOME_PAGE_URL_EHABGROUP
from scraper.websites.twob import HOME_PAGE_URL_TWOB
from django.db import DataError
# add the project directory to the Python path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pcwd/'))
if project_path not in sys.path:
    sys.path.append(project_path)
# set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings')
django.setup()
from product.models import Website, ScrapedProduct


website_amazon, _ = Website.objects.get_or_create(name='AM', country='EG', url=HOME_PAGE_URL_AMAZON)
website_jumia, _ = Website.objects.get_or_create(name='JU', country='EG', url=HOME_PAGE_URL_JUMIA)
website_ehabgroup, _ = Website.objects.get_or_create(name='EH', country='EG', url=HOME_PAGE_URL_EHABGROUP)
website_twob, _ = Website.objects.get_or_create(name='2B', country='EG', url=HOME_PAGE_URL_TWOB)


def import_products_from_csv(file_path_en, file_path_ar):
    # read English and Arabic CSV files into DataFrames
    df_en = pd.read_csv(file_path_en).drop_duplicates()
    df_ar = pd.read_csv(file_path_ar).drop_duplicates()

    # print column names to verify they are as expected
    print("English CSV Columns:", df_en.columns)
    print("Arabic CSV Columns:", df_ar.columns)

    # normalize the URLs by removing 'ar/' in the Arabic DataFrame
    df_en['normalized_url'] = df_en['product_url'].apply(normalize_url)
    df_ar['normalized_url'] = df_ar['product_url'].apply(normalize_url)

    # set the normalized URLs as the index for easy lookup
    df_en.set_index('normalized_url', inplace=True)
    df_ar.set_index('normalized_url', inplace=True)

    # iterate over the English DataFrame and match with the Arabic DataFrame
    for new_index, row_en in df_en[6490:].iterrows():
        try:
            # get the corresponding Arabic row using the normalized URL
            row_ar = df_ar.loc[new_index]

            website = None
            if 'amazon' in row_en['product_url']:
                website = website_amazon
            elif 'jumia' in row_en['product_url']:
                website = website_jumia
            elif 'ehabgroup' in row_en['product_url']:
                website = website_ehabgroup
            elif '2b' in row_en['product_url']:
                website = website_twob

            # create ScrapedProduct instance
            scraped_product = ScrapedProduct.objects.create(
                website=website,
                image_url=remove_latin_letters(row_en['image_url']),
                price=safe_float_conversion(remove_latin_letters(row_en['price'])),
            )

            # English translation
            scraped_product.translations.create(
                language_code='en',
                description=remove_latin_letters(row_en['description']),  # adjust length as needed
                brand=remove_latin_letters(row_en['brand']),
                color=remove_latin_letters(row_en['color']),
                currency=remove_latin_letters(row_en['currency']),
            )

            scraped_product.translation.create(
                language_code='en',
                product_url=remove_latin_letters(row_en['product_url']),
            )

            # Arabic translation
            scraped_product.translations.create(
                language_code='ar',
                description=remove_latin_letters(row_ar['description']),  # adjust length as needed
                brand=remove_latin_letters(row_ar['brand']),
                color=remove_latin_letters(row_ar['color']),
                currency=remove_latin_letters(row_ar['currency']),
            )

            scraped_product.translation.create(
                language_code='ar',
                product_url=remove_latin_letters(row_ar['product_url']),
            )

        except KeyError as e:
            print(f"KeyError: {e} - corresponding row not found in Arabic csv")
            continue   # skip saving the row if not found in Arabic csv
        except DataError as e:
            print(f"DataError: {e} at index : {new_index} - data too long for field constraints")


# call the function with the paths to the English and Arabic CSV files
import_products_from_csv('scraper/products-en.csv', 'scraper/products-ar.csv')
