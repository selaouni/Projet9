from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    pass
    #account_number = CharField(max_length=10, unique=True)
