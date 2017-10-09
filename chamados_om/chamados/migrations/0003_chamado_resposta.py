# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0002_auto_20171009_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='resposta',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
