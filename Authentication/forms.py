from dataclasses import fields
from distutils.command.clean import clean
from email.policy import default
from mimetypes import init
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CreatePasienForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        

class CreateDokterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',  'password1', 'password2']