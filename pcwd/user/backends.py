from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Custom authentication backend to allow login with either email or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # ensure both username and password are provided
        if username is None or password is None:
            return None

        user = None
        # try to fetch the user by email
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # if no user is found, try to fetch by username
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        # check the password and return the user if valid
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
