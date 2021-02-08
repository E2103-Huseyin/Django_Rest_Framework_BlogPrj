from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,ProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Profile
# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "user"
    