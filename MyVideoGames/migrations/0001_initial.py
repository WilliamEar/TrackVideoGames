# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 13:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('gender', models.PositiveIntegerField(choices=[(0, 'MALE'), (1, 'FEMALE'), (2, 'UNKNOWN')], default=3, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyVideoGames.Console')),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyVideoGames.Franchise')),
            ],
        ),
        migrations.AddField(
            model_name='platform',
            name='video_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyVideoGames.VideoGame'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='video_game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyVideoGames.VideoGame'),
        ),
        migrations.AddField(
            model_name='appear',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyVideoGames.Character'),
        ),
        migrations.AddField(
            model_name='appear',
            name='video_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyVideoGames.VideoGame'),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('video_game', 'user')]),
        ),
    ]