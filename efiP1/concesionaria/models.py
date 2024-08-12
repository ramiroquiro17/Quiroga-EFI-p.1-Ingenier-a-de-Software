from django.db import models
from django.contrib.auth.models import User
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)  

    numero_de_puertas = models.IntegerField()
    cilindrada = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_de_combustible = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.marca.nombre} {self.modelo.nombre}'

class Comentario(models.Model):
    auto = models.ForeignKey(
        Auto,
        on_delete=models.CASCADE,
        related_name='comentarios',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return f'comentario de {self.author.username} para {self.auto.modelo} {self.auto.marca}'
    
class Sede(models.Model):
    nombre = models.CharField(max_length=200)
    ciudad_id = models.ForeignKey('Ciudad', on_delete=models.CASCADE)
    gerente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.direccion} - {self.ciudad_id}"