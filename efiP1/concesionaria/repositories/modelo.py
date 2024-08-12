from typing import List, Optional, NoReturn

from concesionaria.models import Modelo

class ModeloRepository:

    def get_all(self) -> List[Modelo]:
        return Modelo.objects.all()

    def get_by_id(self, id: int) -> Optional[Modelo]:
        return Modelo.objects.get(pk=id)

    def delete(self, modelo: Modelo):
        modelo.delete()

    def update(
        self,
        modelo: Modelo,
        nombre: str,
    ):
        modelo.nombre = nombre
        modelo.save()

    def create(
        self,
        nombre: str
    ) -> Modelo:
        modelo = Modelo.objects.filter(nombre=nombre)
        if modelo:
            return "Este modelo ya fue registrado"
        return Modelo.objects.create(
            nombre=nombre,
        )


