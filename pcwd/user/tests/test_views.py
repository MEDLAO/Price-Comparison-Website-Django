import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from user.models import Profile


User = get_user_model()


@pytest.mark.django_db
def test_add_to_favorite_authenticated(client, create_test_user, scraped_product):
    """
    Tests that an authenticated user can add a product to favorites.
    """
    user = create_test_user
    profile = Profile.objects.get(user=user)
    client.force_login(user)
    # call the add_to_favorite view
    response = client.post(reverse('user:add-to-favorite-en', args=[scraped_product.id]))
    assert response.status_code == 302
    assert scraped_product in profile.favorite_products.all()


@pytest.mark.django_db
def test_add_to_favorite_unauthenticated(client, scraped_product):
    """
    Tests that an unauthenticated user cannot add a product to favorites.
    """
    # attempt to call the add_to_favorite view without logging in
    response = client.post(reverse('user:add-to-favorite-en', args=[scraped_product.id]))
    assert response.status_code == 302
    assert response.url == f'/accounts/login/?next=/favorites/en/add-to-favorite/{scraped_product.id}/'


@pytest.mark.django_db
def test_remove_from_favorite_authenticated(client, create_test_user, scraped_product):
    """
    Tests that an authenticated user can remove a product from favorites.
    """
    user = create_test_user
    client.force_login(user)

    # add the scraped product to the user's favorites
    profile = Profile.objects.get(user=user)
    profile.favorite_products.add(scraped_product)
    # call the remove_from_favorite view
    response = client.post(reverse('user:remove-from-favorite-en', args=[scraped_product.id]))
    assert response.status_code == 302
    assert scraped_product not in profile.favorite_products.all()


@pytest.mark.django_db
def test_favorites_list_authenticated(client, create_test_user, scraped_product):
    """
    Tests that the favorites list is displayed for authenticated users.
    """
    user = create_test_user
    client.force_login(user)

    # add the scraped product to favorites
    profile = Profile.objects.get(user=user)
    profile.favorite_products.add(scraped_product)

    # call the favorites list view
    response = client.get(reverse('user:favorites-list-en'))
    content = response.content.decode()
    assert response.status_code == 200
    assert "Your Favorite Smartwatches" in content
    assert scraped_product.description in content


@pytest.mark.django_db
def test_favorites_list_unauthenticated(client):
    """
    Tests that an unauthenticated user cannot access the favorites list.
    """
    # call the favorites list view without logging in
    response = client.get(reverse('user:favorites-list-en'))
    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/favorites/en/'
