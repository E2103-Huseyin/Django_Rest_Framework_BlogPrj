from django.urls import path
from .views import PostList,PostDetail,PostCreate,Comment,View,CreateLikeAPI,PostUpdate,PostDelete

urlpatterns = [
    path('list/', PostList.as_view(), name ="list"),
    path('detail/<str:slug>/', PostDetail.as_view(), name ="detail"),
    path('create/', PostCreate.as_view(), name ="create"),
    path('comment/', Comment.as_view(), name ="comment"),
    path('view/', View.as_view(), name ="view"),
    path('like/<str:slug>/', CreateLikeAPI.as_view(), name ="like"),
    path('update/<str:slug>/', PostUpdate.as_view(), name ="update"),
    path('delete/<str:slug>/', PostDelete.as_view(), name ="delete"),
    
]