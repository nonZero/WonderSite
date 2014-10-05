# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='priority',
            field=models.PositiveIntegerField(default=3, choices=[(5, b'Very high'), (4, b'High'), (3, b'Normal'), (2, b'Low'), (1, b'Very low')]),
            preserve_default=True,
        ),
    ]
