from typing import List, Optional, NoReturn

from concesionaria.models import Marca

class MarcaRepository:

    def get_all(self) -> List[Marca]:
        return Marca.objects.all()

    def get_by_id(self, id: int) -> Optional[Marca]:
        return Marca.objects.get(pk=id)

    def delete(self, marca: Marca):
        marca.delete()

    def update(
        self,
        marca: Marca,
        nombre: str,
    ):
        marca.nombre = nombre
        marca.save()

    def create(
        self,
        nombre: str
    ) -> Marca:
        marca = Marca.objects.filter(nombre=nombre)
        if marca:
            return "Esta marca ya fue registrada"
        return Marca.objects.create(
            nombre=nombre,
        )

