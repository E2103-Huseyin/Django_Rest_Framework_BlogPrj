from django.contrib import admin
from .models import PostBlog,PostComment,PostView,PostLike

# Register your models here.

admin.site.register(PostBlog)
admin.site.register(PostComment)
admin.site.register(PostView)
admin.site.register(PostLike)
