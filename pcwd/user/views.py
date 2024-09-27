from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from product.models import ScrapedProduct


@login_required
def add_to_favorite(request, product_id):
    product = get_object_or_404(ScrapedProduct, id=product_id)
    profile = request.user.profile
    profile.favorite_products.add(product)

    language = 'en' if '/en/' in request.path else 'ar'
    if language == 'en':
        return redirect('user:favorites-list-en')
    else:
        return redirect('user:favorites-list-ar')


@login_required
def remove_from_favorite(request, product_id):
    product = get_object_or_404(ScrapedProduct, id=product_id)
    profile = request.user.profile
    profile.favorite_products.remove(product)

    language = 'en' if '/en/' in request.path else 'ar'
    if language == 'en':
        return redirect('user:favorites-list-en')
    else:
        return redirect('user:favorites-list-ar')


@login_required
def favorites_list(request):
    profile = request.user.profile
    language = 'en' if '/en/' in request.path else 'ar'
    favorites = profile.favorite_products.language(language).all()
    template_name = 'favorites_list_en.html' if language == 'en' else 'favorites_list_ar.html'
    return render(request, template_name, {'favorites': favorites})
