from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    # Display these fields in the admin user list
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    # Fields to be displayed when viewing a user in the admin
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be displayed when adding a new user in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

    # Allow searching for users by email and username
    search_fields = ('email', 'username')
    ordering = ('email',)

# Register the CustomUser model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)


# Register the Profile model in the admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
    search_fields = ('user__username', 'user__email')

