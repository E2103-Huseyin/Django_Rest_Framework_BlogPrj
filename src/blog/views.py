from django.shortcuts import render
from rest_framework import generics
from .serializers import PostListSerializer,PostCreateSerializer,CommentSerializer,PostViewSerializer
from .models import PostBlog,PostComment,PostView

# Create your views here.
class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset= PostBlog.objects.all()
    
    # def get_queryset(self):
    #     queryset= PostBlog.objects.all()
    #     title = self.kwargs["title"]
    #     queryset = queryset.filter(postblog__title=title)
    #     return queryset
    
    
class PostCreate(generics.CreateAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = PostCreateSerializer
    # permission_classes = [IsAdminUser]   
    
    def perform_create(self, serializer): #https://www.django-rest-framework.org/api-guide/generic-views/
        serializer.save(blogger=self.request.user)

class Comment(generics.CreateAPIView):
    queryset= PostComment.objects.all()
    serializer_class = CommentSerializer
    
    
class View(generics.CreateAPIView):
    queryset= PostView.objects.all()
    serializer_class = PostViewSerializer