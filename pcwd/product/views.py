from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q, Min
from .models import ScrapedProduct


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

        search_query = self.request.GET.get('q')
        if search_query:
            search_terms = search_query.split()
            query = Q()
            for term in search_terms:
                query |= Q(translations__description__icontains=term)
            queryset = queryset.filter(query)

        # group by price and description, and get the minimum id for each group
        distinct_products = queryset.values('price', 'translations__description').annotate(
            min_id=Min('id')
        )

        # retrieve the distinct products based on the min_id
        unique_product_ids = [item['min_id'] for item in distinct_products]
        unique_products = ScrapedProduct.objects.language(language).filter(
            id__in=unique_product_ids).order_by('price')

        return unique_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context
