from datetime import datetime
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    LOW = "LW"
    INTERMEDIATE = "IM"
    HIGH = "HH"
    IMPORTANCE_CHOICES = [
        (LOW, 'Low'),
        (INTERMEDIATE, 'Intermediate'),
        (HIGH, 'High'),
    ]
    importance = models.CharField(
        max_length = 2, 
        choices = IMPORTANCE_CHOICES,
        default = LOW
    )
    time = models.DateTimeField(auto_now_add = True)
    title = models.TextField()
    description = models.TextField()
