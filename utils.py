import os
import sys
import django
import pandas as pd
# add the project directory to the Python path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pcwd/'))
if project_path not in sys.path:
    sys.path.append(project_path)
# set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings')
django.setup()
from product.models import Website, ScrapedProduct


EHABGROUP_URL_EN = "https://ehabgroup.com/smart-wearables.html"

website_eh_en, _ = Website.objects.get_or_create(name='EH', country='EG', url=EHABGROUP_URL_EN)


def import_products_from_csv(file_path_en, file_path_ar):
    # read English and Arabic CSV files into DataFrames
    df_en = pd.read_csv(file_path_en)
    df_ar = pd.read_csv(file_path_ar)

    # print column names to verify they are as expected
    print("English CSV Columns:", df_en.columns)
    print("Arabic CSV Columns:", df_ar.columns)

    # normalize the URLs by removing 'ar/' in the Arabic DataFrame
    df_en['normalized_url'] = df_en['product_url']
    df_ar['normalized_url'] = df_ar['product_url'].apply(lambda x: x.replace('ar/', ''))

    # set the normalized URLs as the index for easy lookup
    df_en.set_index('normalized_url', inplace=True)
    df_ar.set_index('normalized_url', inplace=True)

    # iterate over the English DataFrame and match with the Arabic DataFrame
    for new_index, row_en in df_en.iterrows():
        # get the corresponding Arabic row using the normalized URL
        row_ar = df_ar.loc[new_index]

        # create ScrapedProduct instance
        scraped_product = ScrapedProduct.objects.create(
            website=website_eh_en,
            image_url=row_en['image_url'],
            price=row_en['price'],
        )

        # English translation
        scraped_product.translations.create(
            language_code='en',
            product_url=row_en['product_url'],
            description=row_en['description'],
            brand=row_en['brand'],
            color=row_en['color'],
            currency=row_en['currency'],
        )

        # Arabic translation
        scraped_product.translations.create(
            language_code='ar',
            product_url=row_ar['product_url'],
            description=row_ar['description'],
            brand=row_ar['brand'],
            color=row_ar['color'],
            currency=row_ar['currency'],
        )


# call the function with the paths to the English and Arabic CSV files
import_products_from_csv('scraper/products-en.csv', 'scraper/products-ar.csv')
