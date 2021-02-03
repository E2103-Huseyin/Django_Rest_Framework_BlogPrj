from django.urls import path
from .views import PostList,PostCreate

urlpatterns = [
    path('list/', PostList.as_view(), name ="list"),
    path('create/', PostCreate.as_view(), name ="create"),
    
]