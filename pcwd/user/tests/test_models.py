import pytest
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


@pytest.mark.django_db
def test_create_user(create_test_user):
    """Test that a regular user can be created."""
    user = create_test_user
    assert user.email == "testuser@abc.com"
    assert user.username == "username_test"
    assert user.check_password("pwabcde8") is True


@pytest.mark.django_db
def test_create_superuser(create_test_superuser):
    """Test that a superuser can be created."""
    superuser = create_test_superuser
    assert superuser.is_superuser is True
    assert superuser.is_staff is True


@pytest.mark.django_db
def test_profile_creation(create_test_user):
    """Test that a profile is created automatically when a user is created."""
    user = create_test_user
    assert Profile.objects.filter(user=user).exists()


@pytest.mark.django_db
def test_default_profile_image(create_test_user):
    """Test that the default profile image is set."""
    user = create_test_user
    profile = Profile.objects.get(user=user)
    assert profile.image == 'default.png'
