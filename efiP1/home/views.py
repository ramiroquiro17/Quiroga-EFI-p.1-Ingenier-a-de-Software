from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
    deactivate
)
from users.models import Profile

def updateLang(request):
     if not request.user.is_anonymous:
            profile = Profile.objects.get(user=request.user)
            lang = profile.language
            activate(lang)

class LogginView(View):
    def get(self ,request):
        return render (
            request,
            'home/login.html'
        ) 
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password
            ) 
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login') 

class LogoutView(View):
    def get(self, request):
        updateLang(request)
        logout(request)
        return redirect('login')
@login_required(login_url='login')
def index_view(request):
    updateLang(request)
    return render(
        request,
        'home/index.html'
    )

class UpdateLang(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        lang = profile.language
        if lang == 'es':
            profile.language = 'en'
        if lang == 'en':
            profile.language = 'es'
        profile.save()
        return redirect(request.META.get('HTTP_REFERER', 'index'))
