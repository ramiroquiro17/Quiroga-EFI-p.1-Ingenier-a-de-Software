from django.contrib import admin
from .models import (
    Marca, Modelo, Categoria, Provincia, Ciudad, 
    Color, Proveedor, Pais, Auto, Comentario, Sede
)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia')
    search_fields = ('nombre', 'provincia__nombre')
    list_filter = ('provincia',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'telefono')

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'color', 'pais', 'precio')
    search_fields = ('marca__nombre', 'modelo__nombre', 'categoria__nombre')
    list_filter = ('marca', 'modelo', 'categoria', 'color', 'pais')
    autocomplete_fields = ('marca', 'modelo', 'categoria', 'color', 'pais')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('auto', 'author', 'date', 'rating')
    search_fields = ('auto__modelo__nombre', 'author__username', 'rating')
    list_filter = ('date', 'rating')

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad_id', 'gerente', 'direccion', 'telefono')
    search_fields = ('nombre', 'gerente', 'ciudad_id__nombre', 'direccion')
    list_filter = ('ciudad_id',)

