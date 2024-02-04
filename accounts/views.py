from django.shortcuts import render

# Create your views here.

def user_login(request):
    context = {}
    return render(request, 'accounts/login-register.html.j2', context)