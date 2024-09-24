from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# listView to display all the posts
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_template_names(self):
        if 'en' in self.request.path:
            return ['feed_en.html']
        elif 'ar' in self.request.path:
            return ['feed_ar.html']
        else:
            return ['feed_en.html']


# createView to handle post submissions
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    success_url = reverse_lazy('feed:post-list')

    def get_template_names(self):
        if 'en' in self.request.path:
            return ['post_form_en.html']
        elif 'ar' in self.request.path:
            return ['post_form_ar.html']
        else:
            return ['post_form_en.html']

    def get_success_url(self):
        if 'en' in self.request.path:
            return reverse_lazy('feed:post-list-en')
        elif 'ar' in self.request.path:
            return reverse_lazy('feed:post-list-ar')
        else:
            return reverse_lazy('feed:post-list-en')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
