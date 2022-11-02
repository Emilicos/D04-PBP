from django.db import models
from Authentication.models import User
# Create your models here.

class BlogpostModel(models.Model):
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

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100)
    opening = models.TextField()
    main = models.TextField()
    closing = models.TextField()