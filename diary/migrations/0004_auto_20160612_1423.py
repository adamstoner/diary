# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20160611_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.Tag'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.Tag'),
        ),
    ]
