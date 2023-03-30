from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Post_Feed,Famille


# Import forms
from .forms import LoginForm, RegisterForm, FeedForm, EditProfileForm, RegisterFamilyForm
# Create your views here.
def home(request):
    if request.method == "POST":
        feedform = FeedForm(request.POST,request.FILES)
        if feedform.is_valid():
            texte = feedform.cleaned_data['texte']
            image = feedform.cleaned_data['image']
            post = Post_Feed(auteur=request.user, texte=texte, image=image)
            post.save()
            return redirect('home')
        else:
            return render(request, 'feed.html', {'error': 'Feed form is not valid'})
    else:
        if request.user.is_authenticated:
            posts_feed = Post_Feed.objects.all().order_by("-date")
            profile = Profile.objects.get(user=request.user)
            ajout = Profile.objects.all().exclude(user=request.user).exclude(user__in=profile.amis.all()).order_by("?")[:2]
            famille = profile.famille
            return render(request, 'feed.html', {'user': request.user,'Posts_Feed':posts_feed,"profile":profile,'ajout': ajout, 'famille': famille})
        else:
            return render(request, 'pageAccueil.html')


def search(request):
    if request.method == 'POST':
        query = request.POST["query"]
        posts_feed = Post_Feed.objects.filter(texte__icontains=query).order_by("-date") if query else Post_Feed.objects.all().order_by("-date")
        # Recherche des profils correspondant à l'utilisateur recherché
        profiles = Profile.objects.filter(user__username__icontains=query) if query else Profile.objects.all()
        profile = Profile.objects.get(user=request.user)
        ajout = Profile.objects.all().exclude(user=request.user).order_by("?")[:2]
        famille = profile.famille
        return render(request, 'feed.html', {'user': request.user, 'Posts_Feed': posts_feed, "profile": profile, 'profiles': profiles,"query":query,'ajout': ajout, 'famille': famille})
    else:
        return redirect('home')

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
                return redirect('login')
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

def profile_famille(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        famille = profile.famille
        profiles = Profile.objects.filter(famille=profile.famille).exclude(user=request.user).exclude(user__in=profile.amis.all()).order_by("?")[:2]
        nb_membre=Profile.objects.filter(famille=profile.famille).count()
        return render(request, 'PageFamille.html', {'user': request.user,'profile': profile, 'famille': famille, 'profiles': profiles, 'nb_membre': nb_membre})
    else: 
        return redirect('PageFamille.html')

def edit_profile(request):
    if request.method == 'POST':
        editProfileForm = EditProfileForm(request.POST)
        if editProfileForm.is_valid():
            username = editProfileForm.cleaned_data['username']
            promo = editProfileForm.cleaned_data['promo']
            nom = editProfileForm.cleaned_data['nom']
            prenom = editProfileForm.cleaned_data['prenom']
            if request.user.username != username and User.objects.filter(username=username).exists():
                return render(request, 'PageModification.html', {'error': 'Username already exists'})
            else:
                user = User.objects.get(username=request.user.username)
                user.username = username
                user.last_name = nom
                user.first_name = prenom
                user.save()
                profile = Profile.objects.get(user=user)
                profile.promo = int(promo)
                profile.save()
                return redirect('edit_profile')
        else:
            return render(request, 'PageModification.html', {'error': 'Edit profile form is not valid'})

    else:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            profile = Profile.objects.get(user=request.user)
            return render(request, 'PageModification.html', {'user': user,'profile': profile})
        else:
            return redirect('login')

def presentation(request):
    return render(request,'PagePresentation.html')

def like(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post_Feed.objects.get(id=post_id)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            status = 0
        else:
            post.likes.add(user)
            status = 1
        # return redirect('home')
        return HttpResponse(str(status)+'-'+str(post.likes.count()))
    else:
        return redirect('home')

def ajout_rapide(request):
    if request.method=='POST':
        user_id=request.POST['user_id']
        ami=User.objects.get(id=user_id)

        profile=Profile.objects.get(user=request.user)
        profile.amis.add(ami)
        return redirect('home')

def register_family(request):
    if request.method == 'POST':
        registerForm = RegisterFamilyForm(request.POST)
        if registerForm.is_valid():
            chef = registerForm.cleaned_data['chef']
            nom = registerForm.cleaned_data['nom']
            drive = registerForm.cleaned_data['drive']
            logo = registerForm.cleaned_data['logo']
            description = registerForm.cleaned_data['description']

            if Famille.objects.filter(nom=nom).exists():
                return render(request, 'famille' , {'error': 'Username already exists'})
            else:
                family = Famille.objects.create_user(nom=nom, logo=logo, description=description,drive=drive)
                family.save()
                return render(request,'feed.html')
        else:
            return render(request, 'PageCréationDeFamille.html', {'error': 'Register form is not valid'})
        return render(request,'feed.html')
    else:
        return render(request, 'PageCréationDeFamille.html')