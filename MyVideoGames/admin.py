# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

admin.site.register(models.VideoGame)
admin.site.register(models.Console)
admin.site.register(models.Character)
admin.site.register(models.Franchise)
admin.site.register(models.Company)
admin.site.register(models.GameEngine)