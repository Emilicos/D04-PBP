from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    anonymous = models.BooleanField()
    title = models.CharField(max_length = 128)
    description = models.TextField()