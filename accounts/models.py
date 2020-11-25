from django.contrib.auth.models import AbstractUser
from django.db import models


class myuser(AbstractUser):
    school = models.CharField(max_length=100)
    cafeteria = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


