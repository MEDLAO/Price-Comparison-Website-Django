from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=150, label=_("Username"))
    profile_image = forms.ImageField(required=False, label=_("Profile Image"))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.save()

        profile_image = self.cleaned_data.get('profile_image')
        if profile_image:
            Profile.objects.update_or_create(user=user, defaults={'profile_image': profile_image})
        return user

