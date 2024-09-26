import pytest
from django.urls import reverse, resolve
from user.views import add_to_favorite, remove_from_favorite, favorites_list


# English url tests
@pytest.mark.django_db
def test_add_to_favorite_url_reverse():
    """
    Tests the reverse URL lookup for adding to favorites in English.
    """
    url = reverse('user:add-to-favorite-en', args=[1])
    assert url == '/en/add-to-favorite/1/'


@pytest.mark.django_db
def test_add_to_favorite_url_resolve():
    """
    Tests that the add to favorite URL resolves to the correct view in English.
    """
    resolver = resolve('/favorites/en/add-to-favorite/1/')
    assert resolver.func == add_to_favorite


@pytest.mark.django_db
def test_remove_from_favorite_url_reverse():
    """
    Tests the reverse URL lookup for removing from favorites in English.
    """
    url = reverse('user:remove-from-favorite-en', args=[1])
    assert url == '/favorites/en/remove-from-favorite/1/'


@pytest.mark.django_db
def test_remove_from_favorite_url_resolve():
    """
    Tests that the remove from favorite URL resolves to the correct view in English.
    """
    resolver = resolve('/favorites/en/remove-from-favorite/1/')
    assert resolver.func == remove_from_favorite


@pytest.mark.django_db
def test_favorites_list_url_reverse():
    """
    Tests the reverse URL lookup for favorites list in English.
    """
    url = reverse('user:favorites-list-en')
    assert url == '/favorites/en/'


@pytest.mark.django_db
def test_favorites_list_url_resolve():
    """
    Tests that the favorites list URL resolves to the correct view in English.
    """
    resolver = resolve('/favorites/en/')
    assert resolver.func == favorites_list


# Arabic url tests
@pytest.mark.django_db
def test_add_to_favorite_url_reverse_ar():
    """
    Tests the reverse URL lookup for adding to favorites in Arabic.
    """
    url = reverse('user:add-to-favorite-ar', args=[1])
    assert url == '/favorites/ar/add-to-favorite/1/'


@pytest.mark.django_db
def test_add_to_favorite_url_resolve_ar():
    """
    Tests that the add to favorite URL resolves to the correct view in Arabic.
    """
    resolver = resolve('/favorites/ar/add-to-favorite/1/')
    assert resolver.func == add_to_favorite


@pytest.mark.django_db
def test_remove_from_favorite_url_reverse_ar():
    """
    Tests the reverse URL lookup for removing from favorites in Arabic.
    """
    url = reverse('user:remove-from-favorite-ar', args=[1])
    assert url == '/favorites/ar/remove-from-favorite/1/'


@pytest.mark.django_db
def test_remove_from_favorite_url_resolve_ar():
    """
    Tests that the remove from favorite URL resolves to the correct view in Arabic.
    """
    resolver = resolve('/favorites/ar/remove-from-favorite/1/')
    assert resolver.func == remove_from_favorite


@pytest.mark.django_db
def test_favorites_list_url_reverse_ar():
    """
    Tests the reverse URL lookup for favorites list in Arabic.
    """
    url = reverse('user:favorites-list-ar')
    assert url == '/favorites/ar/'


@pytest.mark.django_db
def test_favorites_list_url_resolve_ar():
    """
    Tests that the favorites list URL resolves to the correct view in Arabic.
    """
    resolver = resolve('/favorites/ar/')
    assert resolver.func == favorites_list
