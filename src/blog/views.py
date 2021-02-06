from django.shortcuts import render
from rest_framework import generics
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateSerializer,CommentSerializer,PostViewSerializer
from .models import PostBlog,PostComment,PostView
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.
class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = PostBlog.objects.all()
    # queryset = Post.objects.filter(status="p")
    permission_classes = [AllowAny]
    
class PostDetail(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer
    queryset = PostBlog.objects.all()
    lookup_field = "slug"
    
   
    
    
class PostCreate(generics.CreateAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = PostCreateSerializer
    # permission_classes = [IsAdminUser]   
    
    def perform_create(self, serializer): #https://www.django-rest-framework.org/api-guide/generic-views/
        serializer.save(blogger=self.request.user)
    


class Comment(generics.CreateAPIView):
    queryset= PostComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    
    
class View(generics.CreateAPIView):
    queryset= PostView.objects.all()
    serializer_class = PostViewSerializer