from datetime import datetime
import re
from django import http
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from urllib3 import Retry
from .forms import CreatePasienForm, CreateDokterForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def chooseRegisterAs(request):
    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('hivcenter:show_homepage')
    return render(request, 'registeras.html')

def registerPasien(request):
    form = CreatePasienForm()
    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('hivcenter:show_homepage')
    if request.method == 'POST':
        form = CreatePasienForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('Authentication:login')
        else:
            messages.error(request, form.errors)
            
    context = {'form':form}
    return render(request, 'registerpasien.html', context)

def registerDokter(request):
    form = CreateDokterForm()
    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('hivcenter:show_homepage')
    if request.method == 'POST':
        form = CreateDokterForm(request.POST)
        if form.is_valid():
            form.instance.role = 2
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('Authentication:login')
        else:
            messages.error(request, form.errors)

    context = {'form':form}
    return render(request, 'registerdokter.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('hivcenter:show_homepage')
    return render(request, 'login.html')

@csrf_exempt
def validate_login(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            data['is_login'] = True
            data['username'] = user.username
            data['role'] = user.role
            print(data)
            return JsonResponse(data)
        else:
            data['is_login'] = False
            return JsonResponse(data)
    return JsonResponse(data)

def logout_user(request):
    logout(request)
    return JsonResponse({
        "message": "successfully logged out"
    })

def show_json(request):
    return JsonResponse(
        {
            "is_login": request.user.is_authenticated,
            "role": request.user.role if request.user.is_authenticated else None,
            "username": request.user.username
            if request.user.is_authenticated
            else None,
        },
        status=200,
    )

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    if data['is_taken']:
        pass
    return JsonResponse(data)