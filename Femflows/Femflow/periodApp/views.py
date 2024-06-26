from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required  # Import login_required
from django.contrib import messages 

def home(request):
    return render(request, 'periodApp/home.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('period-main')
        else:
            messages.error(request, 'Incorrect username or password')  
            return redirect('period-login')
    return render(request, 'periodApp/login.html')

def signup(request):
    if request.method=='POST':
        Fname=request.POST.get('fullName')
        Uname=request.POST.get('username')
        dob=request.POST.get('dob')
        question=request.POST.get('usedBefore')
        email=request.POST.get('email')
        pword=request.POST.get('password')
        cpword=request.POST.get('confirmPassword')
        
        if User.objects.filter(username=Uname).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this username or email already exists.')
            return redirect('period-signup')
        
        if pword != cpword:
            messages.error(request, 'Passwords do not match')  
            return redirect('period-signup')  
        else:
            myuser = User.objects.create_user(username= Uname, email=email, password=pword)
            myuser.save()  
            return redirect('period-after')
        
    return render(request, 'periodApp/Signup.html')

def about(request):
    return render(request,'periodApp/about.html')

@login_required
def main(request):
    username = request.user.username
    return render(request, 'periodApp/main.html',{'username': username})
        
def after(request):
    return render(request, 'periodApp/after.html')

def logoutPage(request):
    logout(request)
    return redirect('period-login')

