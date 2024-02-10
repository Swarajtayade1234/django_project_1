from django.db import models

# Create your models here.

class Data(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    City = models.CharField(max_length=100)
    Email = models.EmailField()
