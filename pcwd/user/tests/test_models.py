import pytest
from django.contrib.auth import get_user_model
from user.models import Profile


User = get_user_model()


@pytest.mark.django_db
def test_create_user(create_test_user):
    """
    Tests that a regular user can be created.
    """
    user = create_test_user
    assert user.email == "testuser@abc.com"
    assert user.username == "username_test"
    assert user.check_password("pwabcde8") is True


@pytest.mark.django_db
def test_create_superuser(create_test_superuser):
    """
    Tests that a superuser can be created.
    """
    superuser = create_test_superuser
    assert superuser.is_superuser is True
    assert superuser.is_staff is True


@pytest.mark.django_db
def test_profile_creation(create_test_user):
    """
    Tests that a profile is created automatically when a user is created.
    """
    user = create_test_user
    assert Profile.objects.filter(user=user).exists()


@pytest.mark.django_db
def test_default_profile_image(create_test_user):
    """
    Tests that the default profile image is set.
    """
    user = create_test_user
    profile = Profile.objects.get(user=user)
    assert profile.image == 'default.png'


@pytest.mark.django_db
def test_add_favorite_product(create_test_user, scraped_product):
    """
    Tests that a product can be added to the user's favorites.
    """
    user = create_test_user
    profile = Profile.objects.get(user=user)
    # add the product to favorites
    profile.favorite_products.add(scraped_product)

    assert scraped_product in profile.favorite_products.all()


@pytest.mark.django_db
def test_remove_favorite_product(create_test_user, scraped_product):
    """
    Tests that a product can be added to the user's favorites.
    """
    user = create_test_user
    profile = Profile.objects.get(user=user)
    # add the product to favorites
    profile.favorite_products.add(scraped_product)
    # then remove the product from favorites
    profile.favorite_products.remove(scraped_product)

    assert scraped_product not in profile.favorite_products.all()


@pytest.mark.django_db
def test_favorite_products_empty(create_test_user):
    """
    Tests that the favorite products list is empty initially.
    """
    user = create_test_user
    profile = Profile.objects.get(user=user)

    # check that the favorite_products field is initially empty
    assert profile.favorite_products.count() == 0
