import os
import sys
import django
import pandas as pd
from scraper.websites.utils import normalize_url
from scraper.websites.amazon import HOME_PAGE_URL_AMAZON
from scraper.websites.jumia import HOME_PAGE_URL_JUMIA
from scraper.websites.ehabgroup import HOME_PAGE_URL_EHABGROUP
from scraper.websites.twob import HOME_PAGE_URL_TWOB
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
    df_en = pd.read_csv(file_path_en)
    df_ar = pd.read_csv(file_path_ar)

    # print column names to verify they are as expected
    print("English CSV Columns:", df_en.columns)
    print("Arabic CSV Columns:", df_ar.columns)

    # normalize the URLs by removing 'ar/' in the Arabic DataFrame
    df_en['normalized_url'] = df_en['product_url'].apply(normalize_url)
    df_ar['normalized_url'] = df_ar['product_url'].apply(normalize_url)

    # set the normalized URLs as the index for easy lookup
    df_en.set_index('normalized_url', inplace=True)
    df_ar.set_index('normalized_url', inplace=True)
    # 1:2, 9605:9606, 11620:11621, 11843:11844
    # iterate over the English DataFrame and match with the Arabic DataFrame
    for new_index, row_en in df_en.iloc[11843:11844].iterrows():
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
            image_url=row_en['image_url'],
            price=row_en['price'],
        )

        # English translation
        scraped_product.translations.create(
            language_code='en',
            description=row_en['description'],
            brand=row_en['brand'],
            color=row_en['color'],
            currency=row_en['currency'],
        )

        scraped_product.translation.create(
            language_code='en',
            product_url=row_en['product_url'],
        )

        # Arabic translation
        scraped_product.translations.create(
            language_code='ar',
            description=row_ar['description'],
            brand=row_ar['brand'],
            color=row_ar['color'],
            currency=row_ar['currency'],
        )

        scraped_product.translation.create(
            language_code='ar',
            product_url=row_ar['product_url'],
        )


# call the function with the paths to the English and Arabic CSV files
import_products_from_csv('scraper/products-en.csv', 'scraper/products-ar.csv')
