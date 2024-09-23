from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import get_language


# listView to display all the posts
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_template_names(self):
        language = get_language()
        if language == 'en':
            return ['feed_en.html']
        else:
            return ['feed_ar.html']


# createView to handle post submissions
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    template_name = 'post_form.html'
    success_url = reverse_lazy('feed:post-list')

    def get_template_names(self):
        language = get_language()
        if language == 'en':
            return ['post_form_en.html']
        else:
            return ['post_form_ar.html']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
