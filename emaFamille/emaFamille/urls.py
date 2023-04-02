"""emaFamille URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homeApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('presentation', views.presentation, name='presentation'),
    path('famille', views.profile_famille, name='famille'),
    path('like', views.like, name='like'),
    path('search', views.search, name='search'),
    path('ajout_rapide', views.ajout_rapide, name='ajout_rapide'),
    path('registerfamily/', views.register_family, name='registerfamily'),
    path('comment', views.comment, name='comment'),
    path('searchfamille', views.searchfamille, name='searchfamille'),
    path('addPendingFamilyRequest', views.add_pending_family_request, name='addPendingFamilyRequest'),
    path('showPendingFamilyRequest', views.show_pending_family_request, name='showPendingFamilyRequest'),
    path('editFamily', views.edit_family, name='editFamily'),
    path('acceptPendingRequest', views.accept_pending_request, name='acceptPendingRequest'),
    path('removeUserFromFamily/<int:user_id>', views.remove_user_from_family, name='removeUserFromFamily'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
