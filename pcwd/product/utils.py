import os
import sys
import django
import pandas as pd
# add the project directory to the Python path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if project_path not in sys.path:
    sys.path.append(project_path)
# set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcwd.settings')
django.setup()
from product.models import Website, ScrapedProduct


EHABGROUP_URL_EN = "https://ehabgroup.com/smart-wearables.html"

website_eh_en, _ = Website.objects.get_or_create(name='EH', country='EG', url=EHABGROUP_URL_EN)


def import_products_from_csv(file_path):
    # read CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # iterate over each row in the DataFrame
    for _, row in df.iterrows():
        # create ScrapedProduct instance
        scraped_product = ScrapedProduct.objects.create(
            website=website_eh_en,
            product_url=row['product_url'],
            image_url=row['image_url'],
            price=row['price'],
        )

        scraped_product.translations.create(
            language_code='en',
            description=row['description'],
            brand=row['brand'],
            color=row['color'],
            currency=row['currency'],
        )


import_products_from_csv('scraper/products.csv')
