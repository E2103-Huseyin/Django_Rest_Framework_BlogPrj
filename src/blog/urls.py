from django.urls import path
from .views import PostList,PostCreate,Comment,View

urlpatterns = [
    path('list/', PostList.as_view(), name ="list"),
    path('create/', PostCreate.as_view(), name ="create"),
    path('comment/', Comment.as_view(), name ="comment"),
    path('view/', View.as_view(), name ="view"),
    
]