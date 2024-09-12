import pytest
from user.forms import CustomSignupForm


@pytest.mark.django_db
def test_form_valid_data():
    """Test that the form is valid with correct data."""
    form = CustomSignupForm(data={
        'email': 'testuser@abc.com',
        'username': 'username_test',
        'password1': 'pwabcde8',
        'password2': 'pwabcde8',
    })
    assert form.is_valid()  # Ensure the form is valid


@pytest.mark.django_db
def test_form_missing_username():
    """Test that the form is invalid without a username."""
    form = CustomSignupForm(data={
        'email': 'testuser@abc.com',
        'password1': 'pwabcde8',
        'password2': 'pwabcde8',
    })
    assert not form.is_valid()
    assert 'username' in form.errors


@pytest.mark.django_db
def test_form_mismatched_passwords():
    """Test that the form is invalid if passwords do not match."""
    form = CustomSignupForm(data={
        'email': 'testuser@abc.com',
        'username': 'username_test',
        'password1': 'pwabcde8',
        'password2': 'wrongpassword123',
    })
    assert not form.is_valid()
    assert 'password2' in form.errors
