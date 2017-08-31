# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0004_auto_20170826_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
        ),
    ]
