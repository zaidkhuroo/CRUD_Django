from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import CreateUser,LoginUser
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
            # return redirect('')
    context={'form':form}    
    return render(request, 'crud_app/registration.html', context=context)

def login(request):
    form = LoginUser()
    if request.method=='GET':
        form = LoginUser(request.GET)
        
        # if form.is_valid():
        #     form.save()
        #     # return redirect('')
    context={'form':form}    
    return render(request, 'crud_app/login.html', context=context)

