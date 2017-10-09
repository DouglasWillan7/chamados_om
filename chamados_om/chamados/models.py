from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Chamado(models.Model):

    motivo = models.CharField(max_length=255, null=False)
    setor = models.CharField(max_length=255, null=False)
    resposta = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('chamado_edit', kwargs={'id': self.id})
