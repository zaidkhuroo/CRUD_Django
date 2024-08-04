from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import CreateUser,LoginUser,Add_record,Update_record
from django.contrib import messages

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from.models import Entries

# Index page view
def index(request):
    # return HttpResponse("Hello!")
    return render(request, 'crud_app/index.html')

#user registration
def register(request):
    form = CreateUser()
    if request.method=='POST':
        form = CreateUser(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Account Created")
            return redirect('login') #this will redirect page to the login page once the user is created
    context={'form':form}    
    return render(request, 'crud_app/registration.html', context=context)

#user login
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
                messages.success(request, "Logged in Successfully") 
            return redirect('dashboard')
    context={'form':form}    
    return render(request, 'crud_app/login.html', context=context)

#user logout
def logout(request):
    auth.logout(request)
    messages.success(request, "You've logged out")
    return redirect('login')

#show a single record
@login_required(login_url='login') #this decorator will let only authenticated users to see the dashboard
def dashboard(request):
    my_entries=Entries.objects.all()
    context={'records': my_entries}
    return render(request, 'crud_app/dashboard.html', context=context)

#add a record
@login_required(login_url='login') #this decorator will let only authenticated users to see the dashboard
def add_record(request):
    form=Add_record()
    if request.method=='POST':
        form=Add_record(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Record Created")
            return redirect('dashboard')
    context={'form':form}
    return render(request, 'crud_app/add_record.html', context=context)


#update record
@login_required(login_url='login') #this decorator will let only authenticated users to see the dashboard
def update_record(request, pk): #this method will take 2 arguments (the request and the primary key id)
    record=Entries.objects.get(id=pk)
    form= Update_record(instance=record)
    if request.method=='POST':
        form=Update_record(request.POST,instance=record) 
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('dashboard')
    context={'form':form}
    return render(request, 'crud_app/update_record.html', context=context)

#view record
@login_required(login_url='login') #this decorator will let only authenticated users to see the dashboard
def view_record(request, pk): #this method will take 2 arguments (the request and the primary key id)
    all_records=Entries.objects.get(id=pk)
    context={'record':all_records}
    return render(request, 'crud_app/view_record.html', context=context)

#delete record
@login_required(login_url='login') #this decorator will let only authenticated users to see the dashboard
def delete_record(request, pk): #this method will take 2 arguments (the request and the primary key id)
     record=Entries.objects.get(id=pk)
     record.delete()
     messages.error(request, "Record Deleted")
     return redirect('dashboard')