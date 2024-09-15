from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
