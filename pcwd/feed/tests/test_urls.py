import pytest
from django.urls import reverse, resolve
from feed.views import PostListView, PostCreateView


@pytest.mark.django_db
def test_post_list_en_url_reverse():
    """Tests that the reverse URL lookup for 'post-list-en' returns the correct path."""
    url = reverse('feed:post-list-en')
    assert url == '/feed/en/'


@pytest.mark.django_db
def test_post_list_en_url_resolve():
    """Tests that the URL '/feed/en/' resolves to the PostListView (English)."""
    resolver = resolve('/feed/en/')
    assert resolver.func.view_class == PostListView


@pytest.mark.django_db
def test_post_list_ar_url_reverse():
    """Tests that the reverse URL lookup for 'post-list-ar' returns the correct path."""
    url = reverse('feed:post-list-ar')
    assert url == '/feed/ar/'


@pytest.mark.django_db
def test_post_list_ar_url_resolve():
    """Tests that the URL '/feed/ar/' resolves to the PostListView (Arabic)."""
    resolver = resolve('/feed/ar/')
    assert resolver.func.view_class == PostListView


@pytest.mark.django_db
def test_post_create_en_url_reverse():
    """Tests that the reverse URL lookup for 'post-create-en' returns the correct path."""
    url = reverse('feed:post-create-en')
    assert url == '/feed/en/post_form/'


@pytest.mark.django_db
def test_post_create_en_url_resolve():
    """Tests that the URL '/feed/en/post_form/' resolves to the PostCreateView (English)."""
    resolver = resolve('/feed/en/post_form/')
    assert resolver.func.view_class == PostCreateView


@pytest.mark.django_db
def test_post_create_ar_url_reverse():
    """Tests that the reverse URL lookup for 'post-create-ar' returns the correct path."""
    url = reverse('feed:post-create-ar')
    assert url == '/feed/ar/post_form/'


@pytest.mark.django_db
def test_post_create_ar_url_resolve():
    """Tests that the URL '/feed/ar/post_form/' resolves to the PostCreateView (Arabic)."""
    resolver = resolve('/feed/ar/post_form/')
    assert resolver.func.view_class == PostCreateView
