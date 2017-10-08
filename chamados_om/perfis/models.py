from django.db import models

# Create your models here.
class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    setor = models.CharField(max_length=255, null=False)


    def convidar(self, perfil_convidado):
        pass

    def get_perfil_logado(request):
        return Perfil.objects.get(id=1)
