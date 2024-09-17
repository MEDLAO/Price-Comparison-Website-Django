from django.urls import path
from .views import PostListView, PostCreateView


app_name = 'feed'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post_form/', PostCreateView.as_view(), name='post-create')
]

