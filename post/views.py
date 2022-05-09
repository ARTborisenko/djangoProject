from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post, CommentPost, Category
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import CommentsFilter


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(moder=True).order_by('-create')


class PostSingle(DetailView):
    model = Post
    context_object_name = 'post'
    queryset = Post.objects.all()


class SomeAction(UpdateView):
    def post(self, request, pk):
        comment = CommentPost()
        post = Post.objects.get(id=pk)
        comment.text = request.POST.__getitem__('text')
        comment.user = User.objects.get(username=request.user.username)
        comment.post = post
        comment.save()
        return redirect(post.get_absolut_url())


class MyComments(LoginRequiredMixin, ListView):
    model = CommentPost
    template_name = "post/post_comments.html"
    context_object_name = 'comments'
    queryset = CommentPost.objects.filter(moder=False)


class SomeAction2(LoginRequiredMixin, UpdateView):

    def post(self, request, pk):
        model = CommentPost.objects.get(id=pk)
        model.moder = True
        model.save()
        return redirect("my_comments")


class MyCommentsAll(LoginRequiredMixin, ListView):
    model = CommentPost
    template_name = "post/post_comments_all.html"
    context_object_name = 'comments'

    def get_filter(self):
        return CommentsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs.filter(post__author=self.request.user)

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class CreatePost(LoginRequiredMixin, CreateView):
    template_name = 'post/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def post(self, request):
        print(request.POST.__getitem__('category'))
        post = Post()
        post.author = User.objects.get(username=request.user.username)
        post.title = request.POST.__getitem__('title')
        post.text = request.POST.__getitem__('text')
        post.category = Category.objects.get(id=request.POST.__getitem__('category'))
        post.moder = False
        post.save()
        return redirect(post.get_absolut_url())


class UpdatePost(LoginRequiredMixin, UpdateView):
    template_name = 'post/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def gt_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        post.title = request.POST.__getitem__('title')
        post.text = request.POST.__getitem__('text')
        post.category = Category.objects.get(id=request.POST.__getitem__('category'))
        post.moder = False
        post.save()
        return redirect(post.get_absolut_url())