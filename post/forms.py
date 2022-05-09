from .models import CommentPost, Post
from django import forms


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('text', 'user', 'post')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
