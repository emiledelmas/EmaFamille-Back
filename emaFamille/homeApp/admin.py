from django.contrib import admin
from .models import Profile,Famille, Post_Feed, Comment, PendingFamilyRequest, PhotoFamille

# Register your models here.
admin.site.register(Profile)
admin.site.register(Famille)
admin.site.register(Post_Feed)
admin.site.register(Comment)
admin.site.register(PendingFamilyRequest)
admin.site.register(PhotoFamille)