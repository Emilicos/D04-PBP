from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatePasienForm, CreateDokterForm

# Create your views here.
def chooseRegisterAs(request):
    return render(request, 'registeras.html')

def registerPasien(request):
    form = CreatePasienForm()

    if request.method == 'POST':
        form = CreatePasienForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'registerpasien.html', context)

def registerDokter(request):
    form = CreateDokterForm()

    if request.method == 'POST':
        form = CreateDokterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'registerpasien.html', context)