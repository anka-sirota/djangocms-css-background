# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CssBackground',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('bg_type', models.CharField(default=b'image', max_length=5, choices=[(b'image', b'image'), (b'rgb', b'rgb'), (b'rgba', b'rgba')])),
                ('r', models.IntegerField(default=0)),
                ('g', models.IntegerField(default=0)),
                ('b', models.IntegerField(default=0)),
                ('a', models.IntegerField(default=0)),
                ('image', filer.fields.image.FilerImageField(default=None, blank=True, to='filer.Image', null=True, verbose_name=b'image')),
            ],
            options={
                'verbose_name': 'css background',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
