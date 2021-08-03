from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=25, null=True)
    point = models.IntegerField(null=True, default=0)
    membership = models.BooleanField(null=True,  default=False)
