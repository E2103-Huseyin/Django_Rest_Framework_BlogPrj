from rest_framework import serializers
from django.http import request
from django.db.models import fields

from .models import PostBlog

class PostListSerializer(serializers.ModelSerializer):
    blogger = serializers.SerializerMethodField() #blogger shows 1 (number). so added this code to see real username
    
    class Meta:
        model = PostBlog
        fields = (
            "id",
            "blogger",
            "title",
            "category",
            "image",
            "content",
            "publish_time",
            "update_time",
            "slug",
        )
        
    def get_blogger(self, obj):#blogger shows 1. so added rhis code to see real username
        return obj.blogger.username 
       
    

      
class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostBlog
        fields = (
            "id",
            # "blogger",
            "title",
            # "category",
            "image",
            "content",
            # "publish_time",
            # "update_time",
            # "slug",
        )
    