from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from random import randint
# from .utils import get_random_code
# import uuid



# Create your models here.


class PostBlog(models.Model):
    EDUCATION = 'EC'
    HEALTH = 'HL'
    FAMILY = 'FM'
    TECHNOLOGY = 'TN'
    ECONOMY = 'EN'
    RELIGION = 'RL'

    BLOG_CATEGORY = [
        (EDUCATION, 'Education'),
        (HEALTH, 'Health'),
        (FAMILY, 'Family'),
        (TECHNOLOGY, 'Technology'),
        (ECONOMY, 'Economy'),
        (RELIGION, 'Religion '),
    ]
    
    DRAFT = 'D'
    PUBLISHED = 'P'
    
    BLOG_STATUS = [
        (DRAFT, 'Draft '),
        (PUBLISHED, 'Published '),
        
    ]
    
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=BLOG_CATEGORY,default=TECHNOLOGY, )
    status = models.CharField(max_length=50, choices=BLOG_STATUS, default=PUBLISHED, )
    image = models.URLField(max_length = 2000, blank=True)
    content = models.TextField()
    publish_time = models.DateField(auto_now_add=True) 
    update_time = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
       
    def save(self, *args, **kwargs):
        if PostBlog.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(PostBlog, self).save(*args, **kwargs)
    
    def comment_text(self):
        return self.postcomment_set.all()
     
    def comment_count(self):
        return self.postcomment_set.all().count()
    
    def view_count(self):
        return self.postview_set.all().count()
    
    def like_count(self):
        return self.postlike_set.all().count()


class PostComment(models.Model):
    comment = models.TextField(max_length=500)
    comment_time = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(PostBlog, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.commenter.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(PostBlog, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(PostBlog, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.user.username