from django.urls import path
from .views import PostList,PostDetail,PostCreate,Comment,View

urlpatterns = [
    path('list/', PostList.as_view(), name ="list"),
    path('detail/<str:slug>', PostDetail.as_view(), name ="detail"),
    path('create/', PostCreate.as_view(), name ="create"),
    path('comment/', Comment.as_view(), name ="comment"),
    path('view/', View.as_view(), name ="view"),
    
]