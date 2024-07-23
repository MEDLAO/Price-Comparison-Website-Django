import pytest
from .models import ScrapedProduct, Website


@pytest.mark.django_db
def test_str_method(scraped_product):
    assert str(scraped_product) == f'{scraped_product.brand} {scraped_product.product_type} ' \
                                   f'- Scraped from {scraped_product.website}'


@pytest.mark.django_db
def test_get_image_upload_path_amazon(scraped_product):
    path = ScrapedProduct.get_image_upload_path(scraped_product, '_AC_SL1500_.jpg')
    assert path == 'amazon/_AC_SL1500_.jpg'

