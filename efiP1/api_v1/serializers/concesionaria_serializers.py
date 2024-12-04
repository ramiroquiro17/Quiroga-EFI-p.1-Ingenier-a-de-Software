from rest_framework import serializers

from concesionaria.models import Auto, Marca, Modelo,Categoria, Color, Pais, Comentario, Proveedor, Sede, Ciudad, Provincia
from django.contrib.auth.models import User

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nombre',)

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('nombre',)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('nombre',)

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('nombre',)

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('nombre',)

class CiudadSerializer(serializers.ModelSerializer):
    #provincia = ProvinciaSerializer()
    class Meta:
        model = Ciudad
        fields = ('nombre',)

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('auto','author','text','date','rating')

class AutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    modelo = ModeloSerializer()
    categoria = CategoriaSerializer()
    color = ColorSerializer()
    pais = PaisSerializer()
    class Meta:
        model = Auto
        fields = ('pk','marca','modelo','categoria','color','pais','numero_de_puertas','cilindrada','tipo_de_combustible','precio')

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('pk','nombre','direccion','telefono')

class SedeSerializer(serializers.ModelSerializer):
    ciudad_id = CiudadSerializer()
    class Meta:
        model = Sede
        fields = ('nombre','ciudad_id','gerente','direccion','telefono')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','username','email','password')