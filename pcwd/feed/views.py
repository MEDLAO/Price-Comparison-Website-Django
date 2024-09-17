from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# listView to display all the posts
class PostListView(ListView):
    model = Post
    template_name = 'feed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10


# createView to handle post submissions
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    template_name = 'post_form.html'
    success_url = reverse_lazy('feed:post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
