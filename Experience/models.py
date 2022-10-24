from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    preview = models.TextField(max_length = 500)
    experience = models.TextField(max_length = 2000)
    
    def __str__(self):
	    return self.title