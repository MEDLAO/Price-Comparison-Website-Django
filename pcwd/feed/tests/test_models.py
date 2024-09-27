import pytest


@pytest.mark.django_db
def test_post_str_method(create_test_post):
    """Tests that the __str__ method of the Post model."""
    post = create_test_post
    assert str(post) == "username_test - Post written for unit tests."
