from perfis.models import Perfil, Convite
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', 
                  {'perfis': Perfil.objects.all(), 
                   'perfil_logado': get_perfil_logado(request)})


def display(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    eh_contato = perfil in perfil_logado.contato.all()

    return render(request, 'perfil.html',
                  {'perfil' : perfil, 
                   'perfil_logado' : get_perfil_logado(request),
                   'eh_contato' : eh_contato})
    

def convidar(request, perfil_id):
    perfil_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidar)
    return redirect(index)


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
