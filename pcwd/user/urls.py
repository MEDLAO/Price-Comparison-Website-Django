from django.urls import path
from .views import add_to_favorite, remove_from_favorite, favorites_list


app_name = 'user'

urlpatterns = [
    path('add-to-favorite/<int:product_id>/', add_to_favorite, name='add-to-favorite'),
    path('remove-from-favorite/<int:product_id>/', remove_from_favorite, name='remove-from-favorite'),
    path('', favorites_list, name='favorites-list'),
]
