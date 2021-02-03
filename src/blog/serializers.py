from rest_framework import serializers
from django.http import request
from django.db.models import fields

from .models import PostBlog

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBlog
        fields = (
            "blogger",
            "title",
            "category",
            "image",
            "content",
            "publish_time",
            "update_time",
            "slug",
        )
        
