from email.policy import default
from random import choices
from xml.sax import default_parser_list
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    PASIEN = 1
    DOKTER = 2

    ROLES = (
        (PASIEN, "pasien"),
        (DOKTER, "dokter"),
    )

    role = models.PositiveIntegerField(choices=ROLES, default=PASIEN)

    def get_is_staff(self):
        return self.is_staff