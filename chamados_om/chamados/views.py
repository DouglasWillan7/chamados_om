from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from chamados.models import Chamado

class ChamadoList(ListView):
    model = Chamado

class ChamadoCreate(CreateView):
    model = Chamado
    success_url = reverse_lazy('chamado_list')
    fields = ['motivo', 'setor']

class ChamadoUpdate(UpdateView):
    model = Chamado
    success_url = reverse_lazy('chamado_list')
    fields = ['motivo', 'setor']

class ChamadoRes(UpdateView):
    model = Chamado
    success_url = reverse_lazy('chamado_list')
    fields = ['motivo', 'setor', 'resposta']

class ChamadoDelete(DeleteView):
    model = Chamado
    success_url = reverse_lazy('chamado_list')
