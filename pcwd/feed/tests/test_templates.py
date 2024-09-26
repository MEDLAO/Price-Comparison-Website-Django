import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_feed_en_template_used(client):
    """
    Tests that the English feed template is used when accessing the English feed page.
    """
    response = client.get(reverse('feed:post-list-en'))
    assert response.status_code == 200
    assert 'feed_en.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_feed_en_template_content(client):
    """
    Tests that the English feed page contains specific content.
    """
    response = client.get(reverse('feed:post-list-en'))
    assert response.status_code == 200
    content = response.content.decode()  # decode byte content to string
    assert "User Feedback Feed" in content
    assert "Write a Post" in content
    assert "Login to write a post" in content


@pytest.mark.django_db
def test_feed_ar_template_used(client):
    """
    Tests that the Arabic feed template is used when accessing the Arabic feed page.
    """
    response = client.get(reverse('feed:post-list-ar'))
    assert response.status_code == 200
    assert 'feed_ar.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_feed_ar_template_content(client):
    """
    Tests that the Arabic feed page contains specific content.
    """
    response = client.get(reverse('feed:post-list-ar'))
    assert response.status_code == 200
    content = response.content.decode()  # decode byte content to string
    assert "تغذية ملاحظات المستخدمين" in content
    assert "اكتب منشوراً" in content
    assert "سجل الدخول لكتابة منشور" in content
