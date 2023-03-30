from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Famille(models.Model):
    nom=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='media/pp', null=True, blank=True)
    description=models.TextField()
    drive=models.CharField(max_length=100)
    chef=models.OneToOneField(User, on_delete=models.DO_NOTHING)
    GPA=models.FloatField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/pp', default="media/pp/default.jpg")
    promo = models.IntegerField()
    famille=models.ForeignKey(Famille, on_delete=models.CASCADE, related_name='Profile', blank=True,null=True)
    def __str__(self):
        return self.user.username


class Post_Feed(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    texte = models.TextField(max_length=360)
    image = models.ImageField(upload_to='media/feed', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    def __str__(self):
        return self.texte

