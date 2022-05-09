from django_filters import FilterSet
from .models import CommentPost


class CommentsFilter(FilterSet):
    class Meta:
        model = CommentPost
        fields = {
            'post': ['exact'],
            'create': ['gte'],
            'user': ['exact'],
            'text': ['icontains'],
            'moder': ['exact'],
        }
