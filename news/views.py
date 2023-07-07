from django.views.generic import ListView, DetailView
from .models import Post


class News(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-timePost')


class Post(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'