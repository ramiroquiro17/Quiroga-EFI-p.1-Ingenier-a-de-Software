from typing import List, Optional, NoReturn

from concesionaria.models import Sede,Ciudad

class SedeRepository:

    def get_all(self) -> List[Sede]:
        return Sede.objects.all()

    def get_by_id(self, id: int) -> Optional[Sede]:
        return Sede.objects.get(pk=id)

    def delete(self, sede: Sede):
        sede.delete()

    def update(
        self,
        sede: Sede,
        nombre: str,
        gerente:str,
        direccion:str,
        telefono:str,
        ciudad_id:Ciudad,
        
    ):
        sede.nombre = nombre
        sede.gerente = gerente
        sede.direccion = direccion
        sede.telefono = telefono
        sede.ciudad_id = ciudad_id
        
        sede.save()

    def create(
        self,
        nombre: str,
        gerente:str,
        direccion:str,
        telefono:str,
        ciudad:Optional[Ciudad]=None,
       
    ):
        sede = Sede.objects.filter(nombre=nombre)
        if sede:
            return "Este nombre de de sede ya existe"
        return Sede.objects.create(
            nombre=nombre,
            gerente=gerente,
            direccion=direccion,
            telefono=telefono,
            ciudad_id=ciudad,
            

        )

