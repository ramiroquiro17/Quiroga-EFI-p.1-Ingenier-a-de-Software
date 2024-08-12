from typing import List, Optional, NoReturn

from concesionaria.models import Categoria

class CategoriaRepository:

    def get_all(self) -> List[Categoria]:
        return Categoria.objects.all()

    def get_by_id(self, id: int) -> Optional[Categoria]:
        return Categoria.objects.get(pk=id)

    def delete(self, categoria: Categoria):
        categoria.delete()

    def update(
        self,
        categoria: Categoria,
        nombre: str,
    ):
        categoria.nombre = nombre
        categoria.save()

    def create(
        self,
        nombre: str
    ) -> Categoria:
        categoria = Categoria.objects.filter(nombre=nombre)
        if categoria:
            return "Este nombre ya es utilizado como categoría"
        return Categoria.objects.create(
            nombre=nombre,
        )

