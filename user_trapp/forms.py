from django import forms
from user_trapp.models import UserProfile
from django.contrib.auth.models import User

class UserProfile_Form(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('user_portfolio', 'profile_pic')

class User_form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')