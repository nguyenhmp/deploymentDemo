# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from ..actors.models import Actor
from .models import Movie, Featured
import datetime
# Create your views here.


def index(req):
	context = {
		"movies":Movie.objects.all()
	}
	return render(req, "actors/moviesIndex.html", context)

def create(req):
	Movie.objects.create(title=req.POST["title"])
	return redirect("/movies")

