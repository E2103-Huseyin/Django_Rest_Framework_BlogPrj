from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from random import randint
# Create your models here.


class PostBlog(models.Model):
    EDUCATION = 'EC'
    HEALTH = 'HL'
    FAMILY = 'FM'
    TECHNOLOGY = 'TN'
    ECONOMY = 'EN'
    RELIGION = 'RL'


    BLOG_CATEGORY = [
        (EDUCATION, 'Education '),
        (HEALTH, 'Health '),
        (FAMILY, 'Family '),
        (TECHNOLOGY, 'Technology '),
        (ECONOMY, 'Economy '),
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
     
    


