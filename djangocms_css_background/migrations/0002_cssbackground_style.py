# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_css_background', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cssbackground',
            name='style',
            field=models.TextField(help_text=b'Additional CSS', null=True, blank=True),
            preserve_default=True,
        ),
    ]
