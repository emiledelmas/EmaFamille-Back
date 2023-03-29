from django.contrib import admin
from .models import Profile,Famille, Post_Feed

# Register your models here.
admin.site.register(Profile)
admin.site.register(Famille)
admin.site.register(Post_Feed)