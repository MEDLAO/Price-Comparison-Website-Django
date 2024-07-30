import pytest
from django.urls import reverse
from django.test import Client
from django.db.models import Max, Q
from pytest_django.asserts import assertTemplateUsed
from .models import ScrapedProduct


@pytest.mark.django_db
def test_product_list_view_search_functionality(client, scraped_product):
    # define the path and send a GET request with a search query
    path = reverse('product-list-en')
    response = client.get(path, {'q': 'Brand'})

    # decode the response content
    content = response.content.decode()

    # expected content (simplified for demonstration)
    expected_content = "English description"

    # perform assertions
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'product_list_en.html')
