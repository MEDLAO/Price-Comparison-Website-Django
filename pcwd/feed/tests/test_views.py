import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from feed.models import Post


User = get_user_model()


@pytest.mark.django_db
def test_post_list_view_authenticated(client, create_test_user, create_test_post):
    """
    Tests that the PostListView displays posts correctly for authenticated users.
    """
    user = create_test_user
    test_post = create_test_post
    client.force_login(user)
    response = client.get(reverse('feed:post-list-en'))

    assert response.status_code == 200
    assert "Share Your Feedback or Ideas" in response.content.decode()
    assert test_post.content in response.content.decode()
    assert '<a href="/feed/en/post_form/" class="button center-button">Write a Post</a>' in\
           response.content.decode()


@pytest.mark.django_db
def test_post_list_view_unauthenticated(client):
    """
    Tests that the PostListView shows the login prompt for unauthenticated users.
    """
    response = client.get(reverse('feed:post-list-en'))
    assert response.status_code == 200
    assert "Share Your Feedback or Ideas" in response.content.decode()
    assert "Login to write a post" in response.content.decode()
    assert '<a href="/feed/en/post_form/" class="button center-button">Write a Post</a>' not in \
           response.content.decode()


@pytest.mark.django_db
def test_post_create_view_authenticated(client, create_test_user):
    """
    Tests that the PostCreateView allows authenticated users to create a post.
    """
    user = create_test_user
    client.force_login(user)

    response = client.post(reverse('feed:post-create-en'), {'content': 'New post for unit tests.'})
    post = Post.objects.first()

    assert response.status_code == 302  # should redirect after post creation
    assert post is not None  # ensure a post was created
    assert post.content == 'New post for unit tests.'
    assert post.user == user


@pytest.mark.django_db
def test_post_create_view_unauthenticated(client):
    """
    Tests that the PostCreateView redirects unauthenticated users to login.
    """
    response = client.get(reverse('feed:post-create-en'))  # access the create view
    assert response.status_code == 302  # should redirect to the login page
    assert response.url == '/accounts/login/?next=/feed/en/post_form/'
