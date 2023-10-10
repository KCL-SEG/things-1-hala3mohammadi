from django.db import models
#from django.contrib.auth.models import AbstractUser

class Thing(models.Model):
    name = models.CharField(max=50)
    description = models.TextField()
    quantity = models.IntegerField()
