"""
Registers the Website, BaseProduct and ScrapedProduct models with the Django admin interface.
"""

from django.contrib import admin
from .models import Website, BaseProduct, ScrapedProduct
from parler.admin import TranslatableAdmin


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'url', 'created_at', 'updated_at')
    list_filter = ('name', 'country')
    search_fields = ('name', 'url')


@admin.register(BaseProduct)
class BaseProductAdmin(TranslatableAdmin):
    list_display = ('product_type', 'price', 'created_at', 'updated_at')
    search_fields = ('translations__description', 'translations__brand', 'translations__color', 'price')
    list_filter = ('product_type', 'created_at')


@admin.register(ScrapedProduct)
class ScrapedProductAdmin(BaseProductAdmin):
    list_display = ('brand', 'product_type', 'website', 'price', 'created_at', 'updated_at')
    search_fields = ('translations__description', 'translations__brand', 'website__name', 'price')
    list_filter = ('website', 'product_type')
