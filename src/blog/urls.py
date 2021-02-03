from django.urls import path
from .views import PostList

urlpatterns = [
    path('list/', PostList.as_view(), name ="list"),
    
]