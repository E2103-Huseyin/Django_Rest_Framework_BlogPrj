from django.contrib import admin
from .models import PostBlog,PostComment

# Register your models here.

admin.site.register(PostBlog)
admin.site.register(PostComment)
