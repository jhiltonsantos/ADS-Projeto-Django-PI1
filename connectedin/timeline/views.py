from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from perfis.models import Perfil, Postagem
from perfis.views import *


class TimelineView(View):
    template_name = 'timeline.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request, self.template_name)


@login_required
def postar(request):
    perfil = get_perfil_logado(request)
    texto = request.GET['texto']
    Postagem.objects.create(perfil=perfil, texto=texto)
    return redirect('index')
    
