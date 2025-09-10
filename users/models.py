from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
# Create your models here.

class Member(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    address=models.TextField(blank=True, null=True)
    phone_number= models.CharField(max_length=20, blank=True, null=True)
    membership_date=models.DateField(auto_now_add=True)
    profile_image=models.ImageField(upload_to='profile_image/', blank=True, null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return self.email

class Author(models.Model):
    name= models.CharField(max_length=100)
    biography=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name