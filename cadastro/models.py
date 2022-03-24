from django.db import models
from django.forms import DateField

# Create your models here.
class Pessoa(models.Model):

    login = models.CharField(max_length=30)

    senha = models.CharField(max_length=100)

    data = models.DateField()

    