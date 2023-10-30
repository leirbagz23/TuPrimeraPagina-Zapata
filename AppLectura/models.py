from django.db import models

# Create your models here.

class Leidos(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)
class Por_Leer(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)
class Leyendo(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)
    


