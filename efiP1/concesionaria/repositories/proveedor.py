from typing import List, Optional, NoReturn

from concesionaria.models import Proveedor

class ProveedorRepository:

    def get_all(self) -> List[Proveedor]:
        return Proveedor.objects.all()

    def get_by_id(self, id: int) -> Optional[Proveedor]:
        return Proveedor.objects.get(pk=id)

    def delete(self, proveedor: Proveedor):
        proveedor.delete()

    def update(
        self,
        proveedor: Proveedor,
        nombre: str,
        direccion:str,
        telefono:str,
    ):
        proveedor.nombre = nombre
        proveedor.direccion = direccion
        proveedor.telefono = telefono
        proveedor.save()

    def create(
        self,
        nombre: str,
        direccion:str,
        telefono:str,
    ) -> Proveedor:
        proveedor = Proveedor.objects.filter(nombre=nombre)
        if proveedor:
            return "Este nombre de proveedor ya existe"
        return Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono
        )


