import pytest
from .models import ScrapedProduct, Website


@pytest.mark.django_db
def test_str_method(scraped_product):
    assert str(scraped_product) == f'{scraped_product.brand} {scraped_product.product_type} ' \
                                   f'- Scraped from {scraped_product.website}'


@pytest.mark.django_db
def test_get_image_upload_path_amazon(scraped_product):
    path = ScrapedProduct.get_image_upload_path(scraped_product, '615LVMteaYL._AC_SL1500_.jpg')
    assert path == 'amazon/615LVMteaYL._AC_SL1500_.jpg'


@pytest.mark.django_db
def test_save_method_download_image(mocker, scraped_product):
    # create a mock response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = b'image_content'

    # patch 'requests.get' in the models module to return the mock response when called
    mocker.patch('.models.requests.get', return_value=mock_response)

    # verify that the image was saved with the correct path
    assert scraped_product.image.name == 'amazon/615LVMteaYL._AC_SL1500_.jpg'

    # verify that the content of the saved image matches the mock response content
    assert scraped_product.image.read() == b'test_image_content'



