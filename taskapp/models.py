from django.db import models
import os

# Create your models here.

class person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='static/images', null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
