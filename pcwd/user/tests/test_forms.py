import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from user.forms import CustomSignupForm


@pytest.mark.django_db
def test_form_valid_data():
    """Test that the form is valid with correct data."""
    form = CustomSignupForm(data={
        'email': 'testuser@example.com',
        'username': 'testuser',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123',
    })
    assert form.is_valid()


@pytest.mark.django_db
def test_form_saves_user():
    """Test that the form saves a user with correct data."""
    form = CustomSignupForm(data={
        'email': 'testuser@example.com',
        'username': 'testuser',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123',
    })
    assert form.is_valid()  # always validate the form first
    user = form.save(request=None)  # save the form data
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'  # check that the email was saved correctly


@pytest.mark.django_db
def test_form_profile_image():
    """Test that the form saves a profile image if provided."""
    profile_image = SimpleUploadedFile(name='test_image.jpg', content=b'testimagecontent', content_type='image/jpeg')
    form = CustomSignupForm(data={
        'email': 'imageuser@example.com',
        'username': 'imageuser',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123',
    }, files={'profile_image': profile_image})

    assert form.is_valid()  # always validate the form first
    user = form.save(request=None)  # save the form data
    assert user.profile.image.name == 'profile_images/test_image.jpg'  # check if the image is saved correctly


@pytest.mark.django_db
def test_form_missing_username():
    """Test that the form is invalid without a username."""
    form = CustomSignupForm(data={
        'email': 'testuser@example.com',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123',
    })
    assert not form.is_valid()  # the form should be invalid without a username
    assert 'username' in form.errors  # ensure the error is related to missing username


@pytest.mark.django_db
def test_form_mismatched_passwords():
    """Test that the form is invalid if passwords do not match."""
    form = CustomSignupForm(data={
        'email': 'testuser@example.com',
        'username': 'testuser',
        'password1': 'strongpassword123',
        'password2': 'wrongpassword123',
    })
    assert not form.is_valid()  # the form should be invalid due to mismatched passwords
    assert 'password2' in form.errors  # the error should be associated with password2
