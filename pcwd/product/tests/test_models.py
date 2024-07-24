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


@pytest.mark.django_db
def test_save_method_download_image(scraped_product):
    # Verify that the image was saved with the correct path
    assert scraped_product.image.name == 'amazon/image.jpg'

    # Verify that the content of the saved image matches the mock response content
    assert scraped_product.image.read() == b'test_image_content'
