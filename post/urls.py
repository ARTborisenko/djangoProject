from django.urls import path
from .views import PostList, PostSingle, SomeAction, MyComments, SomeAction2, MyCommentsAll, CreatePost, UpdatePost

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>', PostSingle.as_view(), name='post_single'),
    path('action/<int:pk>', SomeAction.as_view(), name='action'),
    path('my_comments/', MyComments.as_view(), name='my_comments'),
    path('action2/<int:pk>', SomeAction2.as_view(), name='action2'),
    path('my_comments_all/', MyCommentsAll.as_view(), name='my_comments_all'),
    path('create/', CreatePost.as_view(), name='post_create'),
    path('create/<int:pk>', UpdatePost.as_view(), name='post_update'),
]
