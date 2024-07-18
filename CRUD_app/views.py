from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import CreateUser,LoginUser

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request, 'crud_app/index.html')

def register(request):
    form = CreateUser()
    if request.method=='POST':
        form = CreateUser(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login') #this will redirect page to the login page once the user is created
    context={'form':form}    
    return render(request, 'crud_app/registration.html', context=context)

def login(request):
    form = LoginUser()
    if request.method=='POST':
        form = LoginUser(request, data=request.POST)
        
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user= authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user) 
            return redirect('dashboard')
    context={'form':form}    
    return render(request, 'crud_app/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login') #this will help us to let only authenticated users toi see the dashboard
def dashboard(request):
    return render(request, 'crud_app/dashboard.html')