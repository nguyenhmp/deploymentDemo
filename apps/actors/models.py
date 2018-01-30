# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class ActorManager(models.Manager):
	def validate(self, reqData):
		errors = []
		if reqData["first_name"] == "":
			errors.append("first_name cant be empty")
		if reqData["last_name"] == "":
			errors.append("last_name cant be empty")
		try :
			dob = datetime.datetime.strptime(reqData["dob"], "%Y-%m-%d")
			today = datetime.datetime.today()
			print dob>today
			if dob > today :
				errors.append("dob cannot be in the future")
		except :
			errors.append("dob cannot be empty")
		return errors
		# 1951-09-25

class Actor(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	dob = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ActorManager()