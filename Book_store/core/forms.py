from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w-full py-2 px-3 rounded-l'
    }))
     
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-2 px-3 rounded-l'
    }))
     
     
    


class SignupForm(UserCreationForm):
    model = User
    fields = ('nickname','username', 'email', 'password1', 'password2')
    
    # nickname = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'nickname',
    #     'class': 'w-full py-2 px-3 rounded-l'
    # }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w-full py-2 px-3 rounded-l'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'email address',
        'class': 'w-full py-2 px-3 rounded-l'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-2 px-3 rounded-l'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'reapeat password',
        'class': 'w-full py-2 px-3 rounded-l'
    }))
    
    
# 1:08:05