"""
Provides fixtures for testing the feed app.
"""

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from feed.models import Post


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
def create_test_post():
    return Post.objects.create(user=create_test_user, content="Post written for unit tests.")
