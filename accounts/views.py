from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *
from store.models import *

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username ,len(username))
        print(password)
        print('------------------------------------')
        if username == '' or username == None or len(username) < 10:
            messages.error(request, 'Invalid Mobile Number. Please try again.')
            return redirect('login')
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')  # Redirect to your home page
            else:
                messages.error(request, 'Mobile or password is incorrect. Please try again.')
                return redirect('login')
                # return render(request, 'accounts/login.html.j2', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html.j2')


def user_register(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        state = request.POST.get('state')
        district = request.POST.get('district')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        password = request.POST.get('password2')

        addr = Address.objects.create(state_id=state, district_id=district, city_id=city, address=address, pincode=pincode)

        user = CustomUser.objects.create_user(address=addr, first_name=first_name, last_name=last_name,mobile=mobile, username=mobile, password=password, email=email)

        login(request, user)

        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('home')  # Redirect to your home page
    else:
        state = State.objects.all()
        district = District.objects.all()
        city = City.objects.all()

        context = {
            'state': state,
            'district': district,
            'city': city,
        }

        return render(request, 'accounts/register.html.j2', context)


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')