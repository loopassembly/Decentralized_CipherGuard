from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Login(forms.Form):
    username = forms.CharField(max_length=100)
    passw = forms.CharField(max_length=100,widget=forms.PasswordInput)
  
    
class CustomerForm(ModelForm):
	class Meta:
		model = Registration
		fields = '__all__'
		exclude = ['user']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CreatePasswordForm(ModelForm):
	class Meta:
		model = Userpassword
		fields = ['platform', 'password']
       
