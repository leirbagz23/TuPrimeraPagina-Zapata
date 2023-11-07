from django.db import models

# Create your models here.
#Los modelos corresponden a libros leidos (Leidos) lectura actual (Leyendo) y libros por leer (Por_Leer)
#Todos los modelos contienen 3 atributos, titulo, autor y año de publicación.
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
    


