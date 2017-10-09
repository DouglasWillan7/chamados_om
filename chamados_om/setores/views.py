from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from setores.models import Setor

class SetorList(ListView):
    model = Setor

class SetorCreate(CreateView):
    model = Setor
    success_url = reverse_lazy('setor_list')
    fields = ['nome']

class SetorUpdate(UpdateView):
    model = Setor
    success_url = reverse_lazy('setor_list')
    fields = ['nome']

class SetorDelete(DeleteView):
    model = Setor
    success_url = reverse_lazy('setor_list')
