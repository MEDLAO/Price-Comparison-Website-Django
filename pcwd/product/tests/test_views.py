import pytest
from django.urls import reverse
from django.test import Client
from django.db.models import Max, Q
from pytest_django.asserts import assertTemplateUsed
from .models import ScrapedProduct


@pytest.mark.django_db
def test_product_list_view_en(client, scraped_product):
    # define the path and send a GET request
    path = reverse('product-list-en')
    response = client.get(path)

    # decode the response content
    content = response.content.decode()
    expected_content = "English description"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'product_list_en.html')


@pytest.mark.django_db
def test_product_list_view_ar(client, scraped_product):
    # define the path and send a GET request
    path = reverse('product-list-ar')
    response = client.get(path)

    # decode the response content
    content = response.content.decode()
    expected_content = "وصف عربي"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'product_list_ar.html')
