"""pcwd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from product.views import home, ProductListView, fetch_recommended_products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('en/products/', ProductListView.as_view(), name='product-list-en'),
    path('ar/products/', ProductListView.as_view(), name='product-list-ar'),
    path('en/recommendations/', fetch_recommended_products, name='fetch-recommended-products-en'),
    path('ar/recommendations/', fetch_recommended_products, name='fetch-recommended-products-ar'),
    path('i18n/', include('django.conf.urls.i18n')),  # needed for locale change
    path('feed/', include('feed.urls')),
    path('favorites/', include('user.urls')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
)


handler404 = 'product.views.custom_404'
handler500 = 'product.views.custom_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
