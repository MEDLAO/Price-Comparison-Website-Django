from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile


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
