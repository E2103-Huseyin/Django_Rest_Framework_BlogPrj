from rest_framework import serializers
from django.http import request
from django.db.models import fields
from django.db.models import Q
# from users.models import Profile

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
    # comment_text = CommentSerializer(many=True, read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(view_name='detail',lookup_field='slug')
    class Meta:
        model = PostBlog
        fields = (
            "id",
            "detail_url",
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
            # "comment_text",
        )
        
    def get_blogger(self, obj):#blogger shows 1. so added rhis code to see real username
        return obj.blogger.username 

class PostDetailSerializer(serializers.ModelSerializer):
    blogger = serializers.SerializerMethodField() #blogger shows 1 (number). so added this code to see real username
    comment_text = CommentSerializer(many=True, read_only=True)
    has_liked = serializers.SerializerMethodField()
    # owner = serializers.SerializerMethodField(read_only=True)
    # update_url = serializers.HyperlinkedIdentityField(
    #     view_name='update',
    #     lookup_field='slug'
    # )
    # like_url = serializers.HyperlinkedIdentityField(
    #     view_name='like',
    #     lookup_field='slug'
    # )
    # delete_url = serializers.HyperlinkedIdentityField(
    #     view_name='delete',
    #     lookup_field='slug'
    # )
    # comment_url = serializers.HyperlinkedIdentityField(
    #     view_name='comment',
    #     lookup_field='slug'
    # )
    class Meta:
        model = PostBlog
        fields = (
            # 'like_url',
            # 'update_url',
            # 'delete_url',
            # 'comment_url',
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
            # 'owner',
            "has_liked",
            "comment_text",
        )
        
    def get_blogger(self, obj):#blogger shows 1. so added rhis code to see real username
        return obj.blogger.username 
    
    # def get_owner(self, obj):
    #     request = self.context['request']
    #     if request.user.is_authenticated:
    #         if obj.author == request.user:
    #             return True
    #         return False
        
    

    def get_has_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Post.objects.filter(Q(like__user=request.user) & Q(like__post=obj)).exists():
                return True
            return False

      
class PostCreateSerializer(serializers.ModelSerializer):
    blogger = serializers.SerializerMethodField(read_only=True)
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
    # def get_blogger(self, obj):
    #     request = self.context['request']
    #     if request.user.is_authenticated:
    #         if obj.author == request.user:
    #             return True
    #         return False


        
        
class PostViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostView
        fields = (
            "id",
            "user",
            "post",
            "time_stamp",
            
        )
    
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostBlog
        fields = (
            
            
            "title",
            "category",
            "image",
            "content",
            
        )
    