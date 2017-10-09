from django.db import models

# Create your models here.
class Setor(models.Model):

    nome = models.CharField(max_length=255, null=False)

    def criar_setor(request):
        pass

    def editar_setor(request):
        pass
