import pytest
from django.urls import reverse, resolve
from product.views import home, ProductListView, fetch_recommended_products


@pytest.mark.django_db
def test_home_url_reverse():
    """
    Tests that the reverse URL lookup for 'home' returns '/'.
    """
    url = reverse('home')
    assert url == '/'


@pytest.mark.django_db
def test_home_url_resolve():
    """
    Tests that the URL '/' resolves to the home view function.
    """
    resolver = resolve('/')
    assert resolver.func == home


@pytest.mark.django_db
def test_product_list_en_url_reverse():
    """
    Tests that the reverse URL lookup for 'product-list-en' returns the correct path.
    """
    url = reverse('product-list-en')
    assert url == '/en/products/'


@pytest.mark.django_db
def test_product_list_en_url_resolve():
    """
    Tests that the URL '/en/products/' resolves to the ProductListView (English).
    """
    resolver = resolve('/en/products/')
    assert resolver.func.view_class == ProductListView


@pytest.mark.django_db
def test_product_list_ar_url_reverse():
    """
    Tests that the reverse URL lookup for 'product-list-ar' returns the correct path.
    """
    url = reverse('product-list-ar')
    assert url == '/ar/products/'


@pytest.mark.django_db
def test_product_list_ar_url_resolve():
    """
    Tests that the URL '/ar/products/' resolves to the ProductListView (Arabic).
    """
    resolver = resolve('/ar/products/')
    assert resolver.func.view_class == ProductListView


@pytest.mark.django_db
def test_recommendations_en_url_reverse():
    """
    Tests that the reverse URL lookup for 'fetch-recommended-products' returns the correct path (English).
    """
    url = reverse('fetch-recommended-products-en')
    assert url == '/en/recommendations/'


@pytest.mark.django_db
def test_recommendations_en_url_resolve():
    """
    Tests that the URL '/en/recommendations/' resolves to the fetch_recommended_products view (English).
    """
    resolver = resolve('/en/recommendations/')
    assert resolver.func == fetch_recommended_products


@pytest.mark.django_db
def test_recommendations_ar_url_reverse():
    """
    Tests that the reverse URL lookup for 'fetch-recommended-products-ar' returns the correct path (Arabic).
    """
    url = reverse('fetch-recommended-products-ar')
    assert url == '/ar/recommendations/'


@pytest.mark.django_db
def test_recommendations_ar_url_resolve():
    """
    Tests that the URL '/ar/recommendations/' resolves to the fetch_recommended_products view (Arabic).
    """
    resolver = resolve('/ar/recommendations/')
    assert resolver.func == fetch_recommended_products
