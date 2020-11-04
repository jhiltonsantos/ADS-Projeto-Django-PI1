from perfis.models import Perfil, Convite
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from perfis.models import Perfil, Postagem


@login_required
def index(request):
    perfil_logado = get_perfil_logado(request)
    context = {}
    context['perfis'] = Perfil.objects.all()
    context['perfil_logado'] = get_perfil_logado(request)
    context['postagens'] = Postagem.objects.all().order_by("-data")
    context['contatos'] = perfil_logado.contatos.all()
    return render(request, 'index.html', context)


@login_required
def display(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    eh_contato = perfil in perfil_logado.contatos.all()

    return render(request, 'perfil.html',
                  {'perfil' : perfil, 
                   'perfil_logado' : get_perfil_logado(request),
                   'eh_contato' : eh_contato,
                   'postagens': Postagem.objects.all().order_by("-data")})
    

@login_required
def convidar(request, perfil_id):
    perfil_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    if perfil_logado != perfil_convidar:
        perfil_logado.convidar(perfil_convidar)
    return redirect(index)


@login_required
def get_perfil_logado(request):
    return request.user.perfil


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

