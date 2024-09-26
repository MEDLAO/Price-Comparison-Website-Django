import pytest
from django.urls import reverse
from product.models import ScrapedProduct


@pytest.mark.django_db
def test_favorites_list_en_template_used(client, create_test_user):
    """
    Tests that the English favorites list template is used.
    """
    user = create_test_user
    client.force_login(user)
    response = client.get(reverse('user:favorites-list-en'))

    assert response.status_code == 200
    assert 'favorites_list_en.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_favorites_list_en_template_content(client, create_test_user, scraped_product, website):
    """
    Tests that the English favorites list page contains specific content.
    """
    user = create_test_user
    client.force_login(user)

    # create a test product and add it to favorites
    product = ScrapedProduct.objects.create(
        description="Test Description",
        product_type="Test Type",
        website=website,
        product_url="http://example.com/product",
        image_url="http://example.com/image.png"
    )

    profile = user.profile  # Access the user's profile
    profile.favorite_products.add(product)
    response = client.get(reverse('user:favorites-list-en'))
    content = response.content.decode()

    assert response.status_code == 200
    assert "Your Favorite Smartwatches" in content
    assert "English description" in content


@pytest.mark.django_db
def test_favorites_list_ar_template_used(client, create_test_user):
    """
    Tests that the Arabic favorites list template is used.
    """
    user = create_test_user
    client.force_login(user)
    response = client.get(reverse('user:favorites-list-ar'))

    assert response.status_code == 200
    assert 'favorites_list_ar.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_favorites_list_ar_template_content(client, create_test_user, scraped_product, website):
    """
    Tests that the Arabic favorites list page contains specific content.
    """
    user = create_test_user
    client.force_login(user)
    profile = user.profile
    profile.favorite_products.add(scraped_product)
    response = client.get(reverse('user:favorites-list-ar'))
    content = response.content.decode()

    assert response.status_code == 200
    assert "ساعاتك الذكية المفضلة" in content
    assert "وصف عربي" in content
