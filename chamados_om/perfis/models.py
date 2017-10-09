from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    usuario = models.OneToOneField(User, related_name="perfil")

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        pass

    def get_perfil_logado(request):
        return Perfil.objects.get(id=1)
