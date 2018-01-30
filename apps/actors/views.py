# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Actor
from ..movies.models import Movie, Featured
import datetime
# Create your views here.
def index(req):
	context = {
		"actors":Actor.objects.all()
	}
	return render(req, "actors/index.html", context)

def create(req):
	print "1951-09-25".split("-")

	# dob = datetime.datetime.strptime(req.POST["dob"], "%Y-%m-%d")
	# print dob
	# today = datetime.date.today()
	errors = Actor.objects.validate(req.POST)
	if errors :
		print "there were errors"
	else:
		Actor.objects.create(first_name=req.POST["first_name"], last_name=req.POST["last_name"], dob=req.POST["dob"])
	return redirect("/actors")
def show(req, actor_id):
	context = {
		"actor":Actor.objects.get(id=actor_id),
		"movies":Movie.objects.all()
	}
	return render(req, "actors/showActor.html", context)

def add_to_movie(req, actor_id):
	Featured.objects.create(actor=Actor.objects.get(id=actor_id), movie=Movie.objects.get(id=req.POST["movie"]))
	return redirect("/actors")