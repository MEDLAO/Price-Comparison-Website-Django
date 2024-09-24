from django.urls import path
from .views import PostListView, PostCreateView


app_name = 'feed'

urlpatterns = [
    path('en/', PostListView.as_view(), name='post-list-en'),
    path('ar/', PostListView.as_view(), name='post-list-ar'),
    path('en/post_form/', PostCreateView.as_view(), name='post-create-en'),
    path('ar/post_form/', PostCreateView.as_view(), name='post-create-ar'),
]
