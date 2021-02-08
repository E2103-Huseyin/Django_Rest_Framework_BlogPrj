from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import PostBlog
from .utils import get_random_code
from rest_framework.authtoken.models import Token


@receiver(pre_save, sender=PostBlog)
def pre_save_create_code(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())
        
@receiver(post_save, sender=User)
def create_token(sender, instance,created, **kwargs):
    if created:
        Token.objects.create(user=instance)