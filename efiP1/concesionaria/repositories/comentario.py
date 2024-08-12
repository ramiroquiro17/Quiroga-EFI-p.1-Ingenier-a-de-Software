from typing import List, Optional

from django.contrib.auth.models import User

from concesionaria.models import Comentario
from concesionaria.repositories.autos import AutoRepository

class ComentarioRepository:

    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()
    def get_by_id(self, id: int) -> Optional[Comentario]:
        try:
            comentario = Comentario.objects.get(id=id)
        except:
            comentario = None
        return comentario

    def create(
        self,
        auto_id: int,
        author: User,
        text: str,
        rating: int
    ) -> Comentario:
        auto_repo = AutoRepository()
        auto = auto_repo.get_by_id(auto_id)
        comentario = Comentario.objects.create(
            auto=auto,
            author=author,
            text=text,
            rating=rating,
        )
        return comentario
    def delete(self, comentario: Comentario):
        return comentario.delete()
