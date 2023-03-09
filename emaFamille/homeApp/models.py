from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/pp', null=True, blank=True)
    promo = models.IntegerField()
    def __str__(self):
        return self.user.username

class Post_Feed(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    texte = models.TextField(max_length=360)
    image = models.ImageField(upload_to='media/feed', null=True, blank=True)
    def __str__(self):
        return self.texte

