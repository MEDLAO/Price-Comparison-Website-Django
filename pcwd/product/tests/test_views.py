import pytest
from django.urls import reverse
from django.test import Client
from django.db.models import Max, Q
from pytest_django.asserts import assertTemplateUsed
from .models import ScrapedProduct


@pytest.mark.django_db
@pytest.mark.parametrize(
    "price, url_name, template, expected_content",
    [
        (2099.00, "product-list-en", "product_list_en.html", "English description"),
        (1000.00, "product-list-en", "product_list_en.html", "English description"),
        (450.00, "product-list-en", "product_list_en.html", "English description"),
        (2099.00, "product-list-ar", "product_list_ar.html", "وصف عربي"),
        (1000.00, "product-list-ar", "product_list_ar.html", "وصف عربي"),
        (450.00, "product-list-ar", "product_list_ar.html", "وصف عربي"),
    ],
)
def test_product_list_view_with_varying_prices(client, scraped_product, price, url_name, template, expected_content):
    # update the price of the scraped_product
    scraped_product.price = price
    scraped_product.save()

    # define the path and send a GET request
    path = reverse(url_name)
    response = client.get(path)

    # decode the response content
    content = response.content.decode()

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, template)


@pytest.mark.django_db
def test_home_view(client):
    path = reverse('home')
    response = client.get(path)

    content = response.content.decode()
    expected_content = "Entry"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
