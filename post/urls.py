from django.contrib import admin
from django.urls import path
from .views import PostList, PostSingle

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>', PostSingle.as_view(), name='post_single')
]
