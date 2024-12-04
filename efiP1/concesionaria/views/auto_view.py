from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
    deactivate
)
from users.models import Profile
from concesionaria.models import Categoria, Modelo, Marca, Pais, Color
from concesionaria.repositories.autos import AutoRepository

repo = AutoRepository()

def updateLang(request):
     if not request.user.is_anonymous:
            profile = Profile.objects.get(user=request.user)
            lang = profile.language
            activate(lang)

def auto_list(request):
    # if not request.user.is_anonymous:
    #         profile = Profile.objects.get(user=request.user)
    #         lang = profile.language
    #         activate(lang)
    updateLang(request)
    autos = repo.get_all()
    return render(
        request,
        'autos/list.html',
        dict(
            autos=autos
        )
    )

def auto_detail(request, id):
    updateLang(request)
    auto = repo.get_by_id(id=id)
    return render(
        request,
        'autos/detail.html',
        {"auto":auto}
    )

def auto_delete(request, id):
    auto = repo.get_by_id(id=id)
    repo.delete(auto=auto)
    return redirect('auto_list')

@login_required(login_url='login')
def auto_update(request, id):
    updateLang(request)
    auto = repo.get_by_id(id)
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    colores = Color.objects.all()
    paises = Pais.objects.all()

    if request.method == "POST":
        
        id_marca = request.POST.get('id_marca')
        id_modelo = request.POST.get('id_modelo')
        id_categoria = request.POST.get('id_categoria')
        id_color = request.POST.get('id_color')
        id_pais = request.POST.get('id_pais')
        numero_de_puertas = request.POST.get('numero_de_puertas')
        cilindrada = request.POST.get('cilindrada')
        tipo_de_combustible = request.POST.get('tipo_de_combustible')
        precio = request.POST.get('precio')
        marca = Marca.objects.get(id=id_marca)
        modelo = Modelo.objects.get(id=id_modelo)
        categoria = Categoria.objects.get(id=id_categoria)
        color = Color.objects.get(id=id_color)
        pais = Pais.objects.get(id=id_pais)

        repo.update(
            auto=auto,
            numero_de_puertas=numero_de_puertas,
            cilindrada=cilindrada,
            tipo_de_combustible=tipo_de_combustible,
            precio = precio,
            marca=marca,
            modelo=modelo,
            categoria=categoria,
            color=color,
            pais=pais
        )

        return redirect('auto_detail', auto.id)  

    
    return render(
        request,
        'autos/update.html',
        {
            'auto': auto,
            'categorias': categorias,
            'marcas': marcas,
            'modelos': modelos,
            'colores': colores,
            'paises': paises
        }
    )

def auto_create(request):
    updateLang(request)
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    colores = Color.objects.all()
    paises = Pais.objects.all()

    if request.method == "POST":       
        id_marca = request.POST.get('id_marca')
        id_modelo = request.POST.get('id_modelo')
        id_categoria = request.POST.get('id_categoria')
        id_color = request.POST.get('id_color')
        id_pais = request.POST.get('id_pais')
        numero_de_puertas = request.POST.get('numero_de_puertas')
        cilindrada = request.POST.get('cilindrada')
        tipo_de_combustible = request.POST.get('tipo_de_combustible')
        precio = request.POST.get('precio')
        marca = Marca.objects.get(id=id_marca)
        modelo = Modelo.objects.get(id=id_modelo)
        categoria = Categoria.objects.get(id=id_categoria)
        color = Color.objects.get(id=id_color)
        pais = Pais.objects.get(id=id_pais)

        auto_nuevo = repo.create(
            marca=marca,
            modelo=modelo,
            categoria=categoria,
            color=color,
            pais=pais,
            numero_de_puertas=numero_de_puertas,
            cilindrada=cilindrada,
            tipo_de_combustible=tipo_de_combustible,
            precio=precio
        )
        return redirect('auto_detail', auto_nuevo.id)

   
    return render(
        request,
        'autos/create.html',
        {
            'marcas': marcas,
            'modelos': modelos,
            'categorias': categorias,
            'colores': colores,
            'paises': paises
        }
    )


def index_view(request):
    return render(
        request,
        'index/index.html'
    )