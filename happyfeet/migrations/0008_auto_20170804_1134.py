# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('happyfeet', '0007_auto_20170804_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myshoe',
            name='shoe_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
