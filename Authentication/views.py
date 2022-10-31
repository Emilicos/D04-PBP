from datetime import datetime
import re
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatePasienForm, CreateDokterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def chooseRegisterAs(request):
    return render(request, 'registeras.html')

def registerPasien(request):
    form = CreatePasienForm()

    if request.method == 'POST':
        form = CreatePasienForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('Authentication:login')
            
    context = {'form':form}
    return render(request, 'registerpasien.html', context)

def registerDokter(request):
    form = CreateDokterForm()

    if request.method == 'POST':
        form = CreateDokterForm(request.POST)
        if form.is_valid():
            form.instance.role = 2
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('Authentication:login')
    context = {'form':form}
    return render(request, 'registerdokter.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.user.is_authenticated:
            messages.info(request, 'Anda sedang login!')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response =  redirect('hivcenter:show_homepage')
                response.set_cookie("last_login", str(datetime.now()))
                return response
            else:
                messages.info(request, 'Username atau Password Salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('Authentication:chooseregisteras')

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