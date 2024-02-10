from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to your home page
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'accounts/login.html.j2', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html.j2')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)

        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('home')  # Redirect to your home page
    else:
        return render(request, 'accounts/register.html.j2')


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home') 