from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    promo = forms.IntegerField(label='promo')
    nom = forms.CharField(label='nom', max_length=100)
    prenom = forms.CharField(label='prenom', max_length=100)