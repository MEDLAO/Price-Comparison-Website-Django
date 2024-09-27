import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_template_used(client):
    """
    Tests that the home template is used when accessing the home page.
    """
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'home.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_home_template_content(client):
    """
    Tests that the home page contains specific content in both Arabic and English.
    """
    response = client.get(reverse('home'))
    assert response.status_code == 200
    content = response.content.decode()  # decode byte content to string
    assert "مقارنة الساعات الذكية" in content
    assert "دخول" in content
    assert "Entry" in content


@pytest.mark.django_db
def test_product_list_en_template_used(client):
    """
    Tests that the English product list template is used when accessing the product list page.
    """
    response = client.get(reverse('product-list-en'))
    assert response.status_code == 200
    assert 'product_list_en.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_product_list_en_template_content(client):
    """
    Tests that the English product list page contains specific content.
    """
    response = client.get(reverse('product-list-en'))
    assert response.status_code == 200
    content = response.content.decode()
    assert "Compare Smart Watches" in content
    assert "Home" in content
    assert "Search" in content
    assert "About" in content
    assert "Contact" in content


@pytest.mark.django_db
def test_product_list_ar_template_used(client):
    """
    Tests that the Arabic product list template is used when accessing the product list page.
    """
    response = client.get(reverse('product-list-ar'))
    assert response.status_code == 200
    assert 'product_list_ar.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_product_list_ar_template_content(client):
    """
    Tests that the Arabic product list page contains specific content.
    """
    response = client.get(reverse('product-list-ar'))
    assert response.status_code == 200
    content = response.content.decode()
    assert "مقارنة الساعات الذكية" in content
    assert "الصفحة الرئيسية" in content
    assert "البحث" in content
    assert "عن الموقع" in content
    assert "اتصل بنا" in content
