from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Entries, CustomUser

#creating user
class CreateUser(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','full_name']

#login user
class LoginUser(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    
#add record
class Add_record(forms.ModelForm):
    class Meta:
        model=Entries
        fields=['title','content','status']
        
#update record
class Update_record(forms.ModelForm):
    class Meta:
        model=Entries
        fields=['title','content','status']