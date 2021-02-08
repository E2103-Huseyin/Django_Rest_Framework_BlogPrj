from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    USERIMG = "https://cdn4.iconfinder.com/data/icons/avatars-xmas-giveaway/128/batman_hero_avatar_comics-128.png"
     
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #OneToOneField => bir kullanıcıya bir profil
    image = models.URLField(max_length = 2000, blank=True, default=USERIMG)
    bio = models.TextField(blank=True)#blank=True => doldurulması zorunlu olmayan text
    
    def __str__(self):
        return self.user.username

 