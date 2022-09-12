from django.db import models


#tablas de nuestra base de datos

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email= models.EmailField()
    telefono = models.CharField(max_length=50)


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()


class Pedidios(models.Model):
    numero= models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
