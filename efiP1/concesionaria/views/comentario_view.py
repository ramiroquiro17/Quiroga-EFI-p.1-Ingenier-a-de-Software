from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from concesionaria.models import Comentario
from concesionaria.repositories.autos import AutoRepository
from concesionaria.repositories.comentario import ComentarioRepository
from users.models import Profile
from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
    deactivate
)

def updateLang(request):
     if not request.user.is_anonymous:
            profile = Profile.objects.get(user=request.user)
            lang = profile.language
            activate(lang)

class ComentarioView(View):
    def get(self, request, *args, **kwargs):
        updateLang(request)
        repo = ComentarioRepository()
        comentarios = repo.get_all()
        return render(
            request,
            'comentarios/list.html',
            dict(
                comentarios=comentarios
            )
        )
    


class ComentarioCreateView(View):
    def get(self, request, *args, **kwargs):
        updateLang(request)
        repo = AutoRepository()
        autos = repo.get_all()
        return render(
            request,
            'comentarios/create.html',
            dict(
                autos=autos
            )
        )
    
    def post(self, request):
        repo = ComentarioRepository()

        auto_id = request.POST.get('auto_id')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        author = request.user

        nuevo_comentario = repo.create(
            auto_id=auto_id,
            author=author,
            text=text,
            rating=rating,
        )
        return redirect('comentario_detail',nuevo_comentario.id )
class ComentarioDetailView(View):
    def get(self, request, id):
        updateLang(request)
        review = get_object_or_404(Comentario, id=id)
        auto = AutoRepository().get_all()
        return render(
            request,
            'comentarios/update.html',
            dict(
                review=review,
                autos=auto
            )
        )
class ComentarioDeleteView(View):
    def get(self, request, id):
        repo = ComentarioRepository()
        comentario = repo.get_by_id(id=id)
        repo.delete(comentario=comentario)
        return redirect('comentario_list')
