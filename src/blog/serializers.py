from rest_framework import serializers
from django.http import request
from django.db.models import fields

from .models import PostBlog,PostComment,PostView,PostLike

class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()
    class Meta:
        model = PostComment
        fields = (
            "id",
            "comment",
            "comment_time",
            "commenter",
            "post",
        )
    def get_commenter(self, obj):#blogger shows 1. so added rhis code to see real username
        return obj.commenter.username 

class PostListSerializer(serializers.ModelSerializer):
    blogger = serializers.SerializerMethodField() #blogger shows 1 (number). so added this code to see real username
    comment_text = CommentSerializer(many=True, read_only=True)
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
            "comment_count",
            "view_count",
            "like_count",
            "comment_text",
        )
        
    def get_blogger(self, obj):#blogger shows 1. so added rhis code to see real username
        return obj.blogger.username 
       
    

      
class PostCreateSerializer(serializers.ModelSerializer):
    # blogger = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PostBlog
        fields = (
            "id",
            "blogger",
            "title",
            "category",
            "image",
            "content",
            # "publish_time",
            # "update_time",
            # "slug",
        )


        
        
class PostViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostView
        fields = (
            "id",
            "user",
            "post",
            "time_stamp",
            "post",
        )
    