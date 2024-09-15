from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')
    list_filter = ('name', 'country')
    search_fields = ('name', 'url')


