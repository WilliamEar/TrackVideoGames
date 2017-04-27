# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Franchise(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    GENDER = ((0, "MALE"), (1, "FEMALE"), (2, "UNKNOWN"))
    gender = models.PositiveIntegerField("Gender", blank=False, default=3, choices=GENDER)

    def __unicode__(self):
        return self.name


class VideoGame(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    franchise = models.ForeignKey(Franchise)

    def __unicode__(self):
        return self.name


class Appear(models.Model):
    character = models.ForeignKey(Character)
    video_game = models.ForeignKey(VideoGame)

    def __unicode__(self):
        return self.character.name + " appears on " + self.video_game.name


class Platform(models.Model):
    video_game = models.ForeignKey(VideoGame)
    console = models.ForeignKey(Console)

    def __unicode__(self):
        return self.video_game.name + " - " + self.console.name


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    class Meta:
        abstract = True


class Favorite(Review):
    video_game = models.ForeignKey(VideoGame, default=1)

    class Meta:
        unique_together = ("video_game", "user")

