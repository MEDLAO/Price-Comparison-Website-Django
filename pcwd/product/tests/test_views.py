import pytest
from django.urls import reverse
from django.test import Client
from django.db.models import Max, Q
from pytest_django.asserts import assertTemplateUsed
from product.models import ScrapedProduct


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url_name, template, expected_content",
    [
        ("product-list-en", "product_list_en.html", "English description"),
        ("product-list-ar", "product_list_ar.html", "وصف عربي"),
        ("home", "home.html", "Entry"),
    ],
)
def test_views_template_used(client, url_name, template, expected_content):
    path = reverse(url_name)
    response = client.get(path)
    content = response.content.decode()

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, template)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "price, expected_to_be_included",
    [
        (300.00, False),  # this should be excluded
        (500.00, True),   # this should be included
    ],
)
def test_product_list_view_excludes_low_price(client, scraped_product, price,
                                              expected_to_be_included):
    # update the price of the scraped_product
    scraped_product.price = price
    scraped_product.save()

    path = reverse('product-list-en')
    response = client.get(path)

    # perform assertions on the queryset
    products = response.context['products']
    assert (scraped_product in products) == expected_to_be_included
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize(
    "price, max_price, expected_to_be_included",
    [
        (450.00, 1000, True),
        (1000.00, 1000, True),
        (2099.00, 1000, False),
    ],
)
def test_product_list_view_max_price_filter(client, scraped_product, price, max_price,
                                            expected_to_be_included):
    # update the price of the scraped_product
    scraped_product.price = price
    scraped_product.save()

    response = client.get(reverse('product-list-en'), {'max_price': max_price})

    # access the queryset from the context
    products = response.context['products']

    assert (scraped_product in products) == expected_to_be_included
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize(
    "language, search_query, expected_to_be_included",
    [
        ('en', 'Brand A', True),
        ('en', 'Brand B', False),
        ('ar', 'العلامة التجارية أ', True),
        ('ar', 'العلامة التجارية ب', False),
    ],
)
def test_product_list_view_search_functionality(client, scraped_product, language, search_query,
                                                expected_to_be_included):
    url_name = f'product-list-{language}'

    response = client.get(reverse(url_name), {'q': search_query})

    products = response.context['products']

    assert any(search_query in product.description for product in products) == expected_to_be_included
    assert response.status_code == 200
