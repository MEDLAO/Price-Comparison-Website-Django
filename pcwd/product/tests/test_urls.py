import pytest
from django.urls import reverse, resolve
from product.views import home, ProductListView


# verify that the url name 'home' correctly maps to '/'
@pytest.mark.django_db
def test_home_url_reverse():
    url = reverse('home')
    assert url == '/'


# verify that the url path '/' correctly maps to the 'home' view function
@pytest.mark.django_db
def test_home_url_resolve():
    resolver = resolve('/')
    assert resolver.func == home


@pytest.mark.django_db
def test_product_list_en_url_reverse():
    url = reverse('product-list-en')
    assert url == '/products/en/'


@pytest.mark.django_db
def test_product_list_en_url_resolve():
    resolver = resolve('/products/en/')
    assert resolver.func.view_class == ProductListView


@pytest.mark.django_db
def test_product_list_ar_url_reverse():
    url = reverse('product-list-ar')
    assert url == '/products/ar/'


@pytest.mark.django_db
def test_product_list_ar_url_resolve():
    resolver = resolve('/products/ar/')
    assert resolver.func.view_class == ProductListView
