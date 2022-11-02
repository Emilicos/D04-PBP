from django.db import models
from Authentication.models import User

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name="patient")
    doctor = models.TextField()
    date = models.DateField()
    time = models.TimeField()