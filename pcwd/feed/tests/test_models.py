import pytest
from feed.models import Post


@pytest.mark.django_db
def test_post_str_method(create_test_post):
    """Tests that the __str__ method of the Post model."""
    post = create_test_post
    assert str(post) == "username_test - Post written for unit tests."
