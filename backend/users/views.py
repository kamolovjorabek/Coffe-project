from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.info(request, "Username or password not given.")
            return redirect("user_login")
        
        user = User.objects.filter(username=username).first()
        if not user:
            messages.error(request, "User not found")
            return redirect("user_login")
        
        user = authenticate(username=username, password=password)
        if not user:
            messages.info(request, "Password incorrect!!")
            return redirect('user_login')
        
        login(request, user)
        return redirect("home")
    
    return render(request, 'login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if not username or not password or not password1:
            messages.info(request, 'Fill in gaps!!!')
            return redirect('user_register')  
        user = User.objects.filter(username=username).first()
        if user:
            messages.info(request, "User has already registered. Go to login.")
            return redirect('user_register')
        if password != password1:
            messages.info(request, "Password must match!")
            return redirect('user_register')  
        User.objects.create_user(username=username, password=password)
        return redirect("user_login")
    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect("home")
