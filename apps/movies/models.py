# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..actors.models import Actor
# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Featured(models.Model):
	movie = models.ForeignKey(Movie, related_name="features")
	actor = models.ForeignKey(Actor, related_name="acted_in")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)