# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20141019_1558'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favouritepost',
            unique_together=set([('post', 'user')]),
        ),
    ]
