from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank = True, null = True)
    date = models.DateField()
    time = models.TimeField()