from django.shortcuts import render, get_list_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import ListView
from django.db.models import Q, Min, Max
from django.core.cache import cache
from .models import ScrapedProduct
from .recommendations import get_recommendations


def home(request):
    return render(request, 'home.html')


class ProductListView(ListView):
    model = ScrapedProduct
    context_object_name = 'products'
    paginate_by = 50

    def get_template_names(self):
        if 'en' in self.request.path:
            return ['product_list_en.html']
        else:
            return ['product_list_ar.html']

    def get_queryset(self):
        language = 'en' if 'en' in self.request.path else 'ar'
        queryset = ScrapedProduct.objects.language(language).exclude(
            image=''
        ).exclude(
            image__isnull=True
        ).exclude(
            price__lt=450
        ).exclude(
            Q(translations__description__icontains='strap') |
            Q(translations__description__icontains='سوار') |
            Q(translations__description__icontains='charger') |
            Q(translations__description__icontains='band') |
            Q(translations__description__icontains='charging cable') |
            Q(translations__description__icontains='charging base')
        )

        search_query = self.request.GET.get('q', '')
        if search_query:
            search_terms = search_query.split()
            query = Q()
            for term in search_terms:
                query |= Q(translations__description__icontains=term)
            queryset = queryset.filter(query)

        max_price = self.request.GET.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        amazon_products = queryset.filter(website__name='AM')

        most_expensive_amazon = amazon_products.order_by('-price')[:50]
        cheapest_amazon = amazon_products.order_by('price')[:50]
        amazon_products_combined = most_expensive_amazon | cheapest_amazon

        queryset = queryset.exclude(website__name='AM')

        combined_queryset = queryset | amazon_products_combined

        distinct_products = combined_queryset.values('price', 'translations__description').annotate(
            min_id=Min('id')
        )

        unique_product_ids = [item['min_id'] for item in distinct_products]
        unique_products = ScrapedProduct.objects.language(language).filter(
            id__in=unique_product_ids).order_by('price')

        return unique_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['max_price'] = self.request.GET.get('max_price')
        context['max_price_db'] = ScrapedProduct.objects.all().aggregate(Max('price'))['price__max']
        return context


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)


def fetch_recommended_products(request):
    # get the product id from the form submission
    product_id = request.GET.get('product_id')

    language = 'en' if '/en/' in request.path else 'ar'

    # fetch the cached recommendations for the product
    cache_key = f'product_recommendations_{product_id}'
    recommended_ids = cache.get(cache_key, [])

    # fetch the recommended products from the database
    recommended_products = ScrapedProduct.objects.language(language).filter(id__in=recommended_ids)

    # determine the correct template based on language
    template_name = 'recommendations_en.html' if language == 'en' else 'recommendations_ar.html'

    return render(request, template_name, {
        'recommended_products': recommended_products,
        'product_id': product_id,
    })
