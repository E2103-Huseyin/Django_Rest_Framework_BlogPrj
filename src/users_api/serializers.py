from rest_framework import serializers
from django.http import request
from django.db.models import fields
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    # email zorunlu olmas için overwrite ettik
    email =serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True, required=True,  style={'input_type':'password'})
    class Meta:
        model = User
        fields = (
            
            "username",
            "email",
            "password",
            "password2"
        )
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password":"Password didn't match"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        
        user.set_password(validated_data["password"])
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "image",
            "bio",
            
        )
    def get_user(self, obj):
        return obj.user.username