from django.shortcuts import render, redirect

from concesionaria.repositories.proveedor import ProveedorRepository

def proveedor_list(request):
    proveedor_repository = ProveedorRepository()
    proveedores = proveedor_repository.get_all()
    return render(
        request,
        'proveedores/list.html',
        dict(
            proveedores=proveedores
        )
    )

def proveedor_detail(request, id:int):
    proveedor_repository = ProveedorRepository()
    proveedor = proveedor_repository.get_by_id(id)
    
    return render(
        request,
        'proveedores/detail.html',
        dict(   
            proveedor=proveedor,
            
        )
    )

def proveedor_delete(request, id: int):
    proveedor_repository = ProveedorRepository()
    proveedor = proveedor_repository.get_by_id(id)
    proveedor_repository.delete(proveedor)
    return redirect('proveedor_list')


def proveedor_update(request, id: int):
    proveedor_repository = ProveedorRepository()
    proveedor = proveedor_repository.get_by_id(id)
    if request.method == 'POST':
        nombre = request.POST.get('name')
        direccion = request.POST.get('addres')
        telefono = request.POST.get('phone')
        proveedor_repository.update(
            proveedor=proveedor,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono
        )
        return redirect('proveedor_list')
    return render(
        request,
        'proveedor/update.html',
        dict(proveedor=proveedor)
    )

def proveedor_create(request):
    proveedor_repository = ProveedorRepository()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        proveedor_repository.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono
        )
        return redirect('proveedor_list')
    return render(
        request,
        'proveedores/create.html',
    )