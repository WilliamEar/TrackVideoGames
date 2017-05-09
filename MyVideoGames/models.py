# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import pycountry

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    COUNTRIES = zip(range(len(pycountry.countries)), [c.name for c in pycountry.countries])
    country = models.PositiveIntegerField("Country", blank=False, default=3, choices=COUNTRIES)

    def __unicode__(self):
        return self.name


class Console(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()
    created_by = models.ForeignKey(Company)

    def __unicode__(self):
        return self.name + " - " + self.created_by.name


class Franchise(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class GameEngine(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class VideoGame(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    franchise = models.ForeignKey(Franchise)
    platform = models.ManyToManyField(Console)
    created_by = models.ForeignKey(Company)
    game_engine = models.ForeignKey(GameEngine)
    genre = models.ForeignKey(Genre)
    cover = models.ImageField(upload_to="MyVideoGames", blank=True, null=True)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    appear = models.ManyToManyField(VideoGame)
    GENDER = ((0, "MALE"), (1, "FEMALE"), (2, "UNKNOWN"))
    gender = models.PositiveIntegerField("Gender", blank=False, default=3, choices=GENDER)

    def __unicode__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    summary = models.TextField()
    body = models.TextField()

    def __unicode__(self):
        return self.title + " - " + self.subtitle

    class Meta:
        abstract = True


class VideoGameNew(New):
    video_game = models.ForeignKey(VideoGame)


class CompanyNew(New):
    company = models.ForeignKey(Company)


class CharacterNew(New):
    character = models.ForeignKey(Character)


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


class Profile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    avatar = models.ImageField(upload_to="avatar", blank=True, null=True)
    favorite_game = models.ForeignKey(VideoGame)

    def __unicode__(self):
        return "Profile of " + str(self.user)

