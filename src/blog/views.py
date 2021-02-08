from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateSerializer,CommentSerializer,PostViewSerializer,PostCreateUpdateSerializer
from .models import PostBlog,PostComment,PostView,PostLike
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .permissions import IsOwner
from blog import serializers

# Create your views here.
class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = PostBlog.objects.all()
    # queryset = Post.objects.filter(status="p")
    permission_classes = [AllowAny]
    
    
    
    
    
    
    
class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer
    queryset = PostBlog.objects.all()
    lookup_field = "slug"
    
class PostUpdate(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [IsAuthenticated]
    queryset = PostBlog.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = "slug"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user) 
    
    
class PostCreate(generics.CreateAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated] 
    # permission_classes = [AllowAny]  
    
    def perform_create(self, serializer): #https://www.django-rest-framework.org/api-guide/generic-views/
        serializer.save(blogger=self.request.user)
    
class PostDelete(generics.DestroyAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
    # permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [IsAuthenticated] 
    
    
    





# class Comment(generics.CreateAPIView):
#     # queryset= PostComment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [AllowAny]
#     # lookup_field = "slug"
#     def get_queryset(self):
#         queryset= PostComment.objects.all()
#         slug = self.kwargs["slug"]
#         queryset = queryset.filter(postblog__slug=slug)
#         return queryset
    
class Comment(APIView):
    """
    post:
        Create a comment instnace. Returns created comment data
        parameters: [slug, body]
    """
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    

    def post(self, request, slug):
        post = get_object_or_404(PostBlog, slug=slug)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(commenter=request.user, post=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)   
    
    
    
class View(generics.CreateAPIView):
    queryset= PostView.objects.all()
    serializer_class = PostViewSerializer
    
    
    

    
class CreateLikeAPI(APIView):

    
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def post(self, request, slug):
        obj = get_object_or_404(PostBlog, slug=slug)
        like_qs = PostLike.objects.filter(user=request.user, post=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            PostLike.objects.create(user=request.user, post=obj)
        data = {
            "messages": "like"
        }
        return Response(data)
    
    
    