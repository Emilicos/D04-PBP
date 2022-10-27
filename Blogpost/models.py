from datetime import datetime
from django.db import models

# Create your models here.

class Importance(models.Model):
    LOW = "LW"
    INTERMEDIATE = "IM"
    HIGH = "HH"
    IMPORTANCE_CHOICES = [
        (LOW, 'Low'),
        (INTERMEDIATE, 'Intermediate'),
        (HIGH, 'High'),
    ]
    status = models.CharField(
        max_length = 2, 
        choices = IMPORTANCE_CHOICES,
        default = LOW
    )

    def __str__(self):
        return self.status
            
class Blogpost(models.Model):
    importance = models.ForeignKey(Importance, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)
    title = models.TextField()
    description = models.TextField()
