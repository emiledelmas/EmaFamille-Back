from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'feed.html', {'user': request.user})
    else:
        return render(request, 'pageAccueil.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'PageConnexion.html', {'error': 'Username or password is incorrect'})
    return render(request, 'PageConnexion.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        promo = request.POST.get('promo')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        if User.objects.filter(username=username).exists():
            return render(request, 'PageInscription.html', {'error': 'Username already exists'})
        else:   
            user = User.objects.create_user(username=username, password=password, email=email,last_name=nom, first_name=prenom)
            user.save()
            profile = Profile(user=user, promo=promo)
            profile.save()
        return redirect('login')
    else:
        return render(request, 'PageInscription.html')
    

def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'PageProfile.html', {'user': request.user,'profile': profile})
    else:
        return redirect('login')