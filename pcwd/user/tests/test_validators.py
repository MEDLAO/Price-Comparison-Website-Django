import pytest
from django.core.exceptions import ValidationError
from user.validators import validate_username, validate_email
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_validate_username_with_existing_email(create_test_user):
    """
    Tests that using an existing email as a username raises a ValidationError.
    """
    test_user = create_test_user
    with pytest.raises(ValidationError) as excinfo:
        validate_username(test_user.email)  # pass the existing user's email as a username
    assert 'This username is already used as an email by another user.' in str(excinfo.value)


@pytest.mark.django_db
def test_validate_email_with_existing_username(create_test_user):
    """
    Tests that using an existing username as an email raises a ValidationError.
    """
    test_user = create_test_user
    with pytest.raises(ValidationError) as excinfo:
        validate_email(test_user.username)  # pass the existing user's username as an email
    assert 'This email is already used as a username by another user.' in str(excinfo.value)
