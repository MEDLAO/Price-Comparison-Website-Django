from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile
from allauth.socialaccount.signals import social_account_added
from django.core.files.base import ContentFile
import requests


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile automatically when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    """
    Saves the profile whenever the user is saved.
    """
    instance.profile.save()


@receiver(social_account_added)
def populate_profile_picture(request, sociallogin, **kwargs):
    # check if the account is a Google account
    if sociallogin.account.provider == 'google':
        # get profile data from the Google account
        profile_picture_url = sociallogin.account.extra_data.get('picture')
        if profile_picture_url:
            # fetch the image data from the URL
            response = requests.get(profile_picture_url)
            if response.status_code == 200:
                # save the image to the Profile model
                user_profile = Profile.objects.get(user=sociallogin.user)
                user_profile.image.save(f"{sociallogin.user.username}_profile.jpg", ContentFile(response.content), save=True)