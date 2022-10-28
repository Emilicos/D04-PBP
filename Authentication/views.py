import re
from django.contrib import messages
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
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('Authentication:login')
    context = {'form':form}
    return render(request, 'registerpasien.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('HIVCenter:show_homepage')
        else:
            messages.info(request, 'Username atau Password Salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('Authentication:chooseregisteras')