from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=150, label=_("Username"))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.save()
        return user

