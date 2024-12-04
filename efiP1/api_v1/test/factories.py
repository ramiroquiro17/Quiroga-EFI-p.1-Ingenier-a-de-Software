import factory
from factory.django import DjangoModelFactory

from concesionaria.models import Auto, Marca, Modelo, Categoria, Color, Pais

class CategoriaFactory(DjangoModelFactory):
    class Meta:
        model = Categoria
    nombre = factory.Sequence(lambda n: f"Categoria {n}")
class MarcaFactory(DjangoModelFactory):
    class Meta:
        model = Marca
    nombre = factory.Sequence(lambda n: f"Marca {n}")

class ModeloFactory(DjangoModelFactory):
    class Meta:
        model = Modelo
    nombre = factory.Sequence(lambda n: f"Modelo {n}")

class ColorFactory(DjangoModelFactory):
    class Meta:
        model = Color
    nombre = factory.Sequence(lambda n: f"Color {n}")

class PaisFactory(DjangoModelFactory):
    class Meta:
        model = Pais
    nombre = factory.Sequence(lambda n: f"Pais {n}")

class AutoFactory(DjangoModelFactory):

    class Meta:
        model = Auto
    marca = factory.SubFactory(MarcaFactory)
    modelo = factory.SubFactory(ModeloFactory)
    categoria = factory.SubFactory(CategoriaFactory)
    color = factory.SubFactory(ColorFactory)
    pais = factory.SubFactory(PaisFactory)

    numero_de_puertas = factory.Iterator([3, 4, 5])
    cilindrada = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)    
    tipo_de_combustible = 'combustible'
    precio = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)

