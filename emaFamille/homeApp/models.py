from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Famille(models.Model):
    nom=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='media/pp',blank=True,null=True)
    description=models.TextField()
    drive=models.URLField(max_length=100,blank=True,null=True)
    chef=models.OneToOneField(User, on_delete=models.CASCADE)
    GPA=models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.nom


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/pp', default="media/pp/default.jpg")
    promo = models.IntegerField()
    famille=models.ForeignKey(Famille, on_delete=models.DO_NOTHING, related_name='Profile', blank=True,null=True)
    amis = models.ManyToManyField(User, related_name='friends', blank=True)
    description = models.TextField(max_length=360, blank=True, null=True)
    def __str__(self):
        return self.user.username


class Post_Feed(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    texte = models.TextField(max_length=360)
    image = models.ImageField(upload_to='media/feed', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    def __str__(self):
        return self.texte
    def nbComment(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post_Feed, on_delete=models.CASCADE, related_name='comments')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.auteur, self.post)
    

class PendingFamilyRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pending_family_requests')
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE, related_name='pending_family_requests')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'pending request from {} to {}'.format(self.user, self.famille)
    
class PhotoFamille(models.Model):
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='media/famille', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    def __str__(self):
        return 'photo of {} on {}'.format(self.famille, self.date)
