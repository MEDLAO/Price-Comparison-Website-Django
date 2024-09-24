from django.urls import path
from .views import add_to_favorite, remove_from_favorite, favorites_list


app_name = 'user'

urlpatterns = [
    path('en/add-to-favorite/<int:product_id>/', add_to_favorite, name='add-to-favorite-en'),
    path('ar/add-to-favorite/<int:product_id>/', add_to_favorite, name='add-to-favorite-ar'),
    path('en/remove-from-favorite/<int:product_id>/', remove_from_favorite, name='remove-from-favorite-en'),
    path('ar/remove-from-favorite/<int:product_id>/', remove_from_favorite, name='remove-from-favorite-ar'),
    path('en/', favorites_list, name='favorites-list-en'),
    path('ar/', favorites_list, name='favorites-list-ar'),
]
