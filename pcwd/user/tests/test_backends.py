import pytest
from django.contrib.auth import authenticate


@pytest.mark.django_db
def test_authenticate_with_email(create_test_user):
    """Test that a user can authenticate using their email."""
    user = authenticate(username='testuser@abc.com', password='pwabcde8')
    assert user is not None
    assert user.email == 'testuser@abc.com'


@pytest.mark.django_db
def test_authenticate_with_username(create_test_user):
    """Test that a user can authenticate using their username."""
    user = authenticate(username='username_test', password='pwabcde8')
    assert user is not None
    assert user.username == 'username_test'


@pytest.mark.django_db
def test_authenticate_with_wrong_credentials(create_test_user):
    """Test that authentication fails with wrong credentials."""
    user = authenticate(username='wrong_email@abc.com', password='wrongpassword')
    assert user is None


@pytest.mark.django_db
def test_authenticate_with_missing_password(create_test_user):
    """Tests that authentication fails when the password is missing."""
    user = authenticate(username='testuser@abc.com', password=None)
    assert user is None


@pytest.mark.django_db
def test_authenticate_with_missing_username(create_test_user):
    """Tests that authentication fails when the username is missing."""
    user = authenticate(username=None, password='pwabcde8')
    assert user is None
