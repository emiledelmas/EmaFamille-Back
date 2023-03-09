from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Profile
# Import forms
from .forms import LoginForm, RegisterForm
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'feed.html', {'user': request.user})
    else:
        return render(request, 'pageAccueil.html')

def login_user(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
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
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data['username']
            password = registerForm.cleaned_data['password']
            email = registerForm.cleaned_data['email']
            promo = registerForm.cleaned_data['promo']
            nom = registerForm.cleaned_data['nom']
            prenom = registerForm.cleaned_data['prenom']
            if User.objects.filter(username=username).exists():
                return render(request, 'PageInscription.html', {'error': 'Username already exists'})
            else:   
                user = User.objects.create_user(username=username, password=password, email=email,last_name=nom, first_name=prenom)
                user.save()
                profile = Profile(user=user, promo=promo)
                profile.save()
        else:
            return render(request, 'PageInscription.html', {'error': 'Register form is not valid'})
        return redirect('login')
    else:
        return render(request, 'PageInscription.html')
    

def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'PageProfile.html', {'user': request.user,'profile': profile})
    else:
        return redirect('login')
    

def edit_profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'PageModification.html', {'user': request.user,'profile': profile})
    else:
        return redirect('login')

def presentation(request):
    return render(request,'PagePresentation.html')
def inscription(request):
    return render(request, 'PageInscription.html')

def connexion(request):
    return render(request, 'PageConnexion.html')