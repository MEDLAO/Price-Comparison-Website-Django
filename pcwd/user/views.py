from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from product.models import ScrapedProduct


@login_required
def add_to_favorite(request, product_id):
    product = get_object_or_404(ScrapedProduct, id=product_id)
    profile = request.user.profile
    profile.favorite_products.add(product)
    return redirect('product-list-en')


@login_required
def remove_from_favorite(request, product_id):
    product = get_object_or_404(ScrapedProduct, id=product_id)
    profile = request.user.profile
    profile.favorite_products.remove(product)
    return redirect('user:favorites-list')


@login_required
def favorites_list(request):
    profile = request.user.profile
    favorites = profile.favorite_products.all()
    return render(request, 'favorites_list.html', {'favorites': favorites})
