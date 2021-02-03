from django.shortcuts import render
from rest_framework import generics
from .serializers import PostListSerializer,PostCreateSerializer
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
    
    
class PostCreate(generics.CreateAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = PostCreateSerializer
    # permission_classes = [IsAdminUser]   
    
    def perform_create(self, serializer): #https://www.django-rest-framework.org/api-guide/generic-views/
        serializer.save(blogger=self.request.user)
    