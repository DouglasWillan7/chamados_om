from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Setor(models.Model):

    nome = models.CharField(max_length=255, null=False)
    data = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'id': self.id})
