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
        ("product-list-en", "product_list_en.html", "Product List - Compare Smart Watches"),
        ("product-list-ar", "product_list_ar.html", "قائمة المنتجات - مقارنة الساعات الذكية"),
        ("home", "home.html", "Entry"),
    ],
)
def test_views_template_used(client, url_name, template, expected_content):
    """
    Tests that the correct template is used and expected content is rendered for different views.
    """
    path = reverse(url_name)
    response = client.get(path)
    content = response.content.decode()

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, template)


# @pytest.mark.django_db
# @pytest.mark.parametrize(
#     "price, expected_to_be_included",
#     [
#         (300.00, False),  # this should be excluded
#         (500.00, True),   # this should be included
#     ],
# )
# def test_product_list_view_excludes_low_price(client, scraped_product, price,
#                                               expected_to_be_included):
#     """
#     Tests that products with a price lower than a threshold are excluded from the product list.
#     """
#     # update the price of the scraped_product
#     scraped_product.price = price
#     scraped_product.save()
#
#     path = reverse('product-list-en')
#     response = client.get(path)
#
#     # perform assertions on the queryset
#     products = response.context['products']
#     assert (scraped_product in products) == expected_to_be_included
#     assert response.status_code == 200


@pytest.mark.django_db
def test_price_greater_than_max_price(client, scraped_product):
    """
    Tests that products with a price higher than the specified max_price are excluded from the product list.
    """
    # update the price of the scraped_product
    scraped_product.price = 1500
    scraped_product.save()

    response = client.get(reverse('product-list-en'), {'max_price': 1000})

    # access the queryset from the context
    products = response.context['products']

    assert not (scraped_product in products)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_price_smaller_than_max_price(client, scraped_product):
#     """
#     Tests that products with a price lower than the specified max_price are included in the product list.
#     """
#     # update the price of the scraped_product
#     scraped_product.price = 700
#     scraped_product.save()
#
#     response = client.get(reverse('product-list-en'), {'max_price': 1000})
#
#     # access the queryset from the context
#     products = response.context['products']
#
#     assert scraped_product in products
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db
# @pytest.mark.parametrize(
#     "language, search_query, expected_to_be_included",
#     [
#         ('en', 'Brand A', True),
#         ('en', 'Brand B', False),
#         ('ar', 'العلامة التجارية أ', True),
#         ('ar', 'العلامة التجارية ب', False),
#     ],
# )
# def test_product_list_view_search_functionality(client, scraped_product, language, search_query,
#                                                 expected_to_be_included):
#     """
#     Tests the search functionality to ensure products are correctly included or excluded based on the search query.
#     """
#     url_name = f'product-list-{language}'
#
#     response = client.get(reverse(url_name), {'q': search_query})
#
#     products = response.context['products']
#
#     assert any(search_query in product.description for product in products) == expected_to_be_included
#     assert response.status_code == 200
