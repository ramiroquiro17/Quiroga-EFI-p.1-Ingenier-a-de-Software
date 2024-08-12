from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from concesionaria.models import Ciudad
from concesionaria.repositories.sede import SedeRepository

repo = SedeRepository()

def sede_list(request):
    sedes = repo.get_all()
    return render(
        request,
        'sedes/list.html',
        dict(
            sedes=sedes
        )
    )

def sede_detail(request, id):
    sede = repo.get_by_id(id=id)
    return render(
        request,
        'sedes/detail.html',
        {"sede":sede}
    )

def sede_delete(request, id):
    sede = repo.get_by_id(id=id)
    repo.delete(sede=sede)
    return redirect('sede_list')

@login_required(login_url='login')
def sede_update(request, id):
    sede = repo.get_by_id(id)
    ciudades = Ciudad.objects.all()

    if request.method == "POST":
        
        id_ciudad = request.POST.get('id_ciudad')
        gerente = request.POST.get('gerente')
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        ciudad = Ciudad.objects.get(id=id_ciudad)
        
        repo.update(
            sede=sede,
            ciudad_id = ciudad,
            gerente=gerente,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
        )

        return redirect('sede_detail', sede.id)  

    
    return render(
        request,
        'sedes/update.html',
        {
            'sede': sede,
            'ciudades':ciudades
        }
    )

def sede_create(request):
    ciudades = Ciudad.objects.all()

    if request.method == "POST":       
        id_ciudad = request.POST.get('id_ciudad')
        gerente = request.POST.get('gerente')
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        ciudad = Ciudad.objects.get(id=id_ciudad)

        sede_nueva = repo.create(
            
            ciudad = ciudad,
            gerente=gerente,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
        )
        return redirect('sede_detail', sede_nueva.id)

   
    return render(
        request,
        'sedes/create.html',
        {
            'ciudades':ciudades
        }
    )


def index_view(request):
    return render(
        request,
        'index/index.html'
    )