from django.db import models

# Create your models here.
class proyecto(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    categoria = models.CharField(max_length=100, null=False)

# Create your models here.
class actividad(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    calificacion = models.CharField(max_length=100, null=False)