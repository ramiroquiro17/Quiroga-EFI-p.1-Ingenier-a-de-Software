from typing import List, Optional

from concesionaria.models import Auto, Categoria, Color, Marca, Modelo, Pais

class AutoRepository:

    def get_all(self) -> List[Auto]:
        return Auto.objects.all()

    def filter_by_id(self, id: int) -> Optional[Auto]:
        return Auto.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Auto]:
        try:
            auto = Auto.objects.get(id=id)
        except:
            auto = None
        return auto

    def get_auto_on_price_range(
        self,
        min_precio: float,
        max_precio: float,
    ) -> List[Auto]:
        #autos = Auto.objects.filter(
        #    price__gt=min_price,
        #    price__lt=max_price,
        #)
        autos = Auto.objects.filter(
            precio__range=(min_precio, max_precio)
        )

        return autos

    def create(
        self,
        precio: float,
        numero_de_puertas:float,
        cilindrada:float,
        tipo_de_combustible:str,
        categoria: Optional[Categoria] = None,
        color:Optional[Color]=None,
        modelo:Optional[Modelo]=None,
        marca:Optional[Marca]=None,
        pais:Optional[Pais]=None,
        

            ):
        return Auto.objects.create(
            precio=precio,
            categoria=categoria,
            color=color,
            modelo=modelo,
            numero_de_puertas=numero_de_puertas,
            cilindrada=cilindrada,
            marca=marca,
            tipo_de_combustible=tipo_de_combustible,
            pais=pais

        )

    def filter_by_category(
        self,
        categoria: Categoria,
    ) -> List[Auto]:
        return Auto.objects.filter(categoria=categoria)

    def filter_by_category_name(
        self,
        nombre_categoria: str,
    ) -> List[Auto]:
        return Auto.objects.filter(
            categoria__nombre=nombre_categoria
        )

    def delete(self, auto: Auto):
        return auto.delete()

    def update(
        self,
        auto: Auto,
        precio: float,
        numero_de_puertas:float,
        cilindrada:float,
        tipo_de_combustible:str,
        categoria: Optional[Categoria] = None,
        color:Optional[Color]=None,
        modelo:Optional[Modelo]=None,
        marca:Optional[Marca]=None,
        pais:Optional[Pais]=None,
    ):
        auto.precio = precio
        auto.numero_de_puertas = numero_de_puertas
        auto.cilindrada = cilindrada
        auto.tipo_de_combustible = tipo_de_combustible
        auto.categoria = categoria
        auto.color = color
        auto.modelo = modelo
        auto.marca = marca
        auto.pais = pais
        auto.save()
