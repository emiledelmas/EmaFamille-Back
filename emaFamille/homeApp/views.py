from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Post_Feed,Famille, Comment, PendingFamilyRequest, PhotoFamille


# Import forms
from .forms import LoginForm, RegisterForm, FeedForm, EditProfileForm, RegisterFamilyForm, SearchForm, EditFamilyForm
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
            comments = Comment.objects.all()
            return render(request, 'feed.html', {'user': request.user,'Posts_Feed':posts_feed,"profile":profile,'ajout': ajout, 'famille': famille,'comments':comments})
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
        if famille is None:
            return redirect('registerfamily')
        else:
            profiles = Profile.objects.filter(famille=profile.famille).exclude(user=request.user).order_by("?")
            nb_membre=Profile.objects.filter(famille=profile.famille).count()
            posts = Post_Feed.objects.filter(auteur__in=Profile.objects.filter(famille=profile.famille).values('user')).order_by("-date")
            pic = PhotoFamille.objects.filter(famille=profile.famille).order_by("?").first()
            comments = Comment.objects.all()
            return render(request, 'PageFamille.html', {'user': request.user,'profile': profile, 'famille': famille, 'profiles': profiles, 'nb_membre': nb_membre, 'posts': posts, 'pic': pic, 'comments': comments})
    else: 
        return redirect('login')

def edit_profile(request):
    if request.method == 'POST':
        editProfileForm = EditProfileForm(request.POST, request.FILES)
        if editProfileForm.is_valid():
            username = editProfileForm.cleaned_data['username']
            promo = editProfileForm.cleaned_data['promo']
            nom = editProfileForm.cleaned_data['nom']
            prenom = editProfileForm.cleaned_data['prenom']
            description = editProfileForm.cleaned_data['description']
            image = editProfileForm.cleaned_data['image']
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
                if description:
                    profile.description = description
                if image:
                    profile.photo = image
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
        registerForm = RegisterFamilyForm(request.POST, request.FILES)
        print(request.FILES)
        if registerForm.is_valid():
            chef = request.user
            nom = registerForm.cleaned_data['nom']
            drive = registerForm.cleaned_data['drive']
            logo = registerForm.cleaned_data['logo']
            description = registerForm.cleaned_data['description']
            if chef.profile.famille is not None:
                return render(request, 'PageCréationDeFamille.html' , {'error': 'You already have a family'})
            elif Famille.objects.filter(nom=nom).exists():
                return render(request, 'PageCréationDeFamille.html' , {'error': 'Family name already taken'})
            else:
                family = Famille(chef=chef,nom=nom, logo=logo, description=description,drive=drive)
                family.save()
                chef.profile.famille = family
                chef.profile.save()
                return redirect('famille')
        else:
            return render(request, 'PageCréationDeFamille.html', {'error': 'Register form is not valid'})
    else:
        profile = Profile.objects.get(user=request.user)
        if profile.famille is not None:
            return redirect('famille')
        else:
            familles = Famille.objects.order_by('?')[:5]
            pending_request = PendingFamilyRequest.objects.filter(user=request.user)
            families_already_asked = Famille.objects.filter(id__in=pending_request.values('famille'))
            return render(request, 'PageCréationDeFamille.html', {'familles': familles, 'families_already_asked': families_already_asked})
    

def comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post_Feed.objects.get(id=post_id)
        user = request.user 
        text = request.POST['text']
        comment = Comment(post=post, auteur=user, body=text)
        comment.save()
        return redirect('home')
    else:
        return redirect('home')
    


def searchfamille(request):
    if request.method == 'POST':
        searchForm = SearchForm(request.POST)
        if searchForm.is_valid():
            nom = searchForm.cleaned_data['query']
            familles = Famille.objects.filter(nom__icontains=nom)
            return render(request, 'PageCréationDeFamille.html', {'familles': familles})
        else:
            return render(request, 'PageCréationDeFamille.html', {'error': 'Search form is not valid'})

def add_pending_family_request(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)
        famille_id = request.POST['famille_id']
        famille = Famille.objects.get(id=famille_id)
        # Check if a PendingFamilyRequest already exists for this user and this family
        if PendingFamilyRequest.objects.filter(user=user, famille=famille).exists():
            # Delete the request
            pendingFamilyRequest = PendingFamilyRequest.objects.get(user=user, famille=famille)
            pendingFamilyRequest.delete()
        else:
            pendingFamilyRequest = PendingFamilyRequest(user=user, famille=famille)
            pendingFamilyRequest.save()
        return redirect('registerfamily')
        

def show_pending_family_request(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        famille = profile.famille
        if profile.famille.chef == user:
            pendingFamilyRequests = PendingFamilyRequest.objects.filter(famille=famille)
            return render(request, 'PageDemandesDeFamille.html', {'pendingFamilyRequests': pendingFamilyRequests, 'famille': famille})
        else:
            return redirect('home') 
    else:
        return redirect('login')


def edit_family(request):
    if request.method == 'POST':
        editFamilyForm = EditFamilyForm(request.POST, request.FILES)
        if editFamilyForm.is_valid():
            nom = editFamilyForm.cleaned_data['nom']
            drive = editFamilyForm.cleaned_data['drive']
            logo = editFamilyForm.cleaned_data['logo']
            description = editFamilyForm.cleaned_data['description']
            chef_id = editFamilyForm.cleaned_data['chef_id']
            famille = Famille.objects.get(chef=request.user)
            if Famille.objects.filter(nom=nom).exclude(id=famille.id).exists():
                famille = Famille.objects.get(chef=request.user)
                users = User.objects.filter(profile__famille=famille).exclude(id=request.user.id)
                return render(request, 'PageModificationFamille.html', {'error': 'Family name already taken'})
            else:
                famille.nom = nom
                famille.description = description
                famille.chef = User.objects.get(id=chef_id)
                famille.drive = drive
                if logo:
                    famille.logo = logo
                famille.save()
                return redirect('famille')
        else:
            famille = Famille.objects.get(chef=request.user)
            users = User.objects.filter(profile__famille=famille).exclude(id=request.user.id)
            return render(request, 'PageModificationFamille.html', {'famille': famille, 'users': users,'error': 'Edit family form is not valid' })
    else:
        if request.user.is_authenticated:
            famille = Famille.objects.get(chef=request.user)
            users = User.objects.filter(profile__famille=famille).exclude(id=request.user.id)
            return render(request, 'PageModificationFamille.html', {'famille': famille, 'users': users})
        else:
            return redirect('login')
        
def accept_pending_request(request):
    if request.method == 'POST':
        # if user is not the chef of the family, redirect to home
        if request.user.profile.famille.chef != request.user:
            return redirect('famille')
        else:
            user_id = request.POST['request_user_id']
            user = User.objects.get(id=user_id)
            famille = Famille.objects.get(chef=request.user)
            profile = Profile.objects.get(user=user)
            profile.famille = famille
            profile.save()
            pendingFamilyRequest = PendingFamilyRequest.objects.get(user=user, famille=famille)
            pendingFamilyRequest.delete()
        return redirect('showPendingFamilyRequest')
    else:
        return redirect('home')
    
def remove_user_from_family(request, user_id):
    if request.method == 'POST':
        # if user is not the chef of the family, redirect to home
        if request.user.profile.famille.chef != request.user:
            return redirect('famille')
        else:
            user = User.objects.get(id=user_id)
            profile = Profile.objects.get(user=user)
            profile.famille = None
            profile.save()
        return redirect('famille')
    else:
        return redirect('home')
    
def album_famille(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        profile = Profile.objects.get(user=request.user)
        famille = profile.famille
        photoFamille = PhotoFamille(photo=photo, famille=famille, user=request.user)
        photoFamille.save()
        return redirect('albumFamille')
    else:
        if request.user.is_authenticated:
            famille = Famille.objects.get(chef=request.user)
            photos = PhotoFamille.objects.filter(famille=famille).order_by('-date')
            return render(request, 'albumFamille.html', {'famille': famille, 'photos': photos})
        else:
            return redirect('login')
        
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post_Feed.objects.get(id=post_id)
        if post.auteur != request.user:
            return redirect('home')
        else:
            post.delete()
            return redirect('home')
    else:
        return redirect('home')