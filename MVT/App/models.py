from django.db import models
import datetime
# Create your models here.
class Familia(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    dni = models.IntegerField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=True)