# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyVideoGames', '0002_auto_20170430_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='MyVideoGames')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='videogame',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='MyVideoGames'),
        ),
    ]
