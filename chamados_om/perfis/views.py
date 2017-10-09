from django.shortcuts import render, redirect
from perfis.models import Perfil
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})

@login_required
def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', { "perfil" : perfil})

@login_required
def get_perfil_logado(request):
    return request.user.perfil
