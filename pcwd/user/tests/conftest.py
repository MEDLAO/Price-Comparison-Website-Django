"""
Provides fixtures for testing the user app.
"""

import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from product.tests.conftest import scraped_product, website


User = get_user_model()


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def create_test_user():
    """Fixture to create a regular test user."""
    return User.objects.create_user(
        email="testuser@abc.com",
        username="username_test",
        password="pwabcde8"
    )


@pytest.fixture
def create_test_superuser():
    """Fixture to create a superuser."""
    return User.objects.create_superuser(
        email="superuser@abc.com",
        username="superuser_username__test",
        password="pwadmin8"
    )
