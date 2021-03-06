from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(moder=True)


class PostSingle(DetailView):
    model = Post
    template_name = 'post/post_single.html'
    context_object_name = 'post'
    queryset = Post.objects.all()
