from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from perfis.models import Perfil, Postagem


class TimelineView(View):
    template_name = 'timeline.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request, self.template_name)
    
    @login_required
    def timeline(request):
        perfil = request.user.perfil
        context = {'perfil' : perfil}
        context['postagens'] = perfil.get_timeline()
        return render(request, 'index.html', context)
        
    