from django.shortcuts import render
from django.views.generic import ListView
from .models import ScrapedProduct


def home(request):
    return render(request, 'home.html')


class ProductListView(ListView):
    model = ScrapedProduct
    context_object_name = 'products'

    def get_template_names(self):
        if 'en' in self.request.path:
            return ['product_list_en.html']
        else:
            return ['product_list_ar.html']

    def get_queryset(self):
        language = 'en' if 'en' in self.request.path else 'ar'
        return ScrapedProduct.objects.order_by('price').language(language).exclude(image='').exclude(image__isnull=True)
