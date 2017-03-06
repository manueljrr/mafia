# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Jailed')], verbose_name='Status')),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='app.Member', verbose_name='Boss')),
                ('jailed_boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member', verbose_name='Jailed boss')),
            ],
        ),
    ]