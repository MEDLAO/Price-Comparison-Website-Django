from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=150, label=_("Username"))
    profile_image = forms.ImageField(required=False, label=_("Profile Image"))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.save()

        profile_image = self.cleaned_data.get('profile_image')
        print(f"Profile Image: {profile_image}")  # Debugging print

        if profile_image:
            user.profile.image = profile_image
            user.profile.save()
            print(f"Profile Image Saved: {user.profile.image.url}")  # Debugging print

        return user
