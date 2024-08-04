import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_template_used(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'home.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_home_template_content(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    content = response.content.decode()  # decode byte content to string
    assert "مقارنة الساعات الذكية" in content
    assert "دخول" in content
    assert "Entry" in content


@pytest.mark.django_db
def test_product_list_en_template_used(client):
    response = client.get(reverse('product-list-en'))
    assert response.status_code == 200
    assert 'product_list_en.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_product_list_en_template_content(client):
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
    response = client.get(reverse('product-list-ar'))
    assert response.status_code == 200
    assert 'product_list_ar.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_product_list_ar_template_content(client):
    response = client.get(reverse('product-list-ar'))
    assert response.status_code == 200
    content = response.content.decode()
    assert "مقارنة الساعات الذكية" in content
    assert "الصفحة الرئيسية" in content
    assert "البحث" in content
    assert "حول" in content
    assert "اتصل" in content
