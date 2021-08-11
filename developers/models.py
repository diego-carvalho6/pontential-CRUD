from django.db import models
# Create your models here.

class Developer(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField()
    hobby = models.CharField(max_length=100)
    datanascimento = models.DateField()