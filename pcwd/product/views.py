from django.shortcuts import render
from django.views.generic import ListView
from .models import ScrapedProduct


class ProductListView(ListView):
    model = ScrapedProduct
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Fetch all products and ensure translations are loaded
        return ScrapedProduct.objects.language('ar').all()
