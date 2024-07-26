from django.contrib.auth.forms import UserCreationForm #provided by django to create users

#to use UserCreationForm we need user model for that which will provide fields and this will be also impoirted from django
from django.contrib.auth.models import User

#using forms
from django import forms

#importing djangos default authentication form 
from django.contrib.auth.forms import AuthenticationForm

#importing username and password widget
from django.forms.widgets import PasswordInput, TextInput

from .models import Entries

#creating user
class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password','password2']

#login user
class LoginUser(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    
#add record
class Add_record(forms.ModelForm):
    class Meta:
        model=Entries
        fields=['title','content','first_name','last_name',]
        
#update record
class Update_record(forms.ModelForm):
    class Meta:
        model=Entries
        fields=['title','content','first_name','last_name',]