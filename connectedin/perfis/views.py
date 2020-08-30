from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil


def index(request):
    return render(request, 'index.html')


def display(request, perfil_id):
    perfil = Perfil()
    if perfil_id == 1:
        perfil = Perfil(perfil_id, 'Hilton', 'hilton@email.com', '555555555', 'ifpi')

    if perfil_id == 2:
        perfil = Perfil(perfil_id, 'Jose', 'jose@email.com',
                        '666666666', 'ifpi')

    return render(request, 'perfil.html', {"perfil": perfil})
