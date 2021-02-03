from django.shortcuts import render
from rest_framework import generics
from .serializers import PostListSerializer
from .models import PostBlog

# Create your views here.
class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset= PostBlog.objects.all()
    
    # def get_queryset(self):
    #     queryset= PostBlog.objects.all()
    #     title = self.kwargs["title"]
    #     queryset = queryset.filter(postblog__title=title)
    #     return queryset
    
    
    
    