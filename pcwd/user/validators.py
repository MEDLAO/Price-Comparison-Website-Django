from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


def validate_username(value):
    """
    Validates that the username is not already used as an email by another user.
    """
    user = get_user_model()
    if user.objects.filter(email=value).exists():
        raise ValidationError('This username is already used as an email by another user.')


def validate_email(value):
    """
    Validates that the email is not already used as a username by another user.
    """
    user = get_user_model()
    if user.objects.filter(username=value).exists():
        raise ValidationError('This email is already used as a username by another user.')
