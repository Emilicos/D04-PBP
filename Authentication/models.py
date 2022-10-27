from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_pasien = models.BooleanField(default=False)
    is_dokter = models.BooleanField(default=False)
    is_rs = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Pasien(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)

class Dokter(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    workPlace = models.CharField(max_length=100)
    workingDays = models.CharField(max_length=50)
    
    def get_dokter_name(self):
        return self.user.first_name + " " + self.user.last_name


class Rumahsakit(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    Location = models.CharField(max_length=100)
