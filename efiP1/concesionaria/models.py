from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name=_('nombre'))

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name=_('nombre'))
    

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name=_('nombre'))

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name=_('nombre'))

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_('nombre'))
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name=_('provincia')) 

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name=_('nombre'))

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, verbose_name=_('nombre'))
    direccion = models.TextField( verbose_name=_('dirección'))
    telefono = models.CharField(max_length=15, verbose_name=_('teléfono'))

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, verbose_name=_('marca'))
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, verbose_name=_('modelo'))
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name=_('categoria'))
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name=_('color'))
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, verbose_name=_('pais'))  

    numero_de_puertas = models.IntegerField(verbose_name=_('número de puertas'))
    cilindrada = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('cilindrada'))
    tipo_de_combustible = models.CharField(max_length=50, verbose_name=_('tipo de combustible'))
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('precio'))

    def __str__(self):
        return f'{self.marca.nombre} {self.modelo.nombre}'

class Comentario(models.Model):
    auto = models.ForeignKey(
        Auto,
        on_delete=models.CASCADE,
        related_name='comentarios',
        verbose_name=_('auto')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('autor'))
    text = models.TextField(verbose_name=_('texto'))
    date = models.DateField(auto_now_add=True, verbose_name=_('fecha'))
    rating = models.IntegerField(verbose_name=_('puntuación'))

    def __str__(self):
        return f'comentario de {self.author.username} para {self.auto.modelo} {self.auto.marca}'
    
class Sede(models.Model):
    nombre = models.CharField(max_length=200, verbose_name=_('nombre'))
    ciudad_id = models.ForeignKey('Ciudad', on_delete=models.CASCADE, verbose_name=_('ciudad'))
    gerente = models.CharField(max_length=100, verbose_name=_('gerente'))
    direccion = models.CharField(max_length=255, verbose_name=_('dirección'))
    telefono = models.CharField(max_length=20, verbose_name=_('teléfono'))

    def __str__(self):
        return f"{self.direccion} - {self.ciudad_id}"

# class AutoImage(models.Model):
#     auto = models.ForeignKey(
#         Auto,
#         on_delete=models.CASCADE, 
#         related_name='images'
#     )
#     image = models.ImageField(upload_to='auto_images/', null=True)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.description or f'Image of {self.auto.marca} {self.auto.modelo}'