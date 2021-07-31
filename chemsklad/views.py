from django.shortcuts import render
from .models import React
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from django.contrib.auth.models import User


def start(request):
    users = User.objects.all()
    return render(request, "start.html", {'users': users})


def login(request):
    if request.method == "POST":
        users_name = list(map(lambda x: x.username, User.objects.all()))
        name = request.POST.get('name')
        if name in users_name:
            return HttpResponseRedirect("/home/")
    return render(request, "No.html")


def index(request):
    return render(request, "index.html")


def notification(request):
    reacts = React.objects.all()
    min_srok = sorted(reacts, key=lambda x: x.srok)[:3]
    min_mass = []
    for i in reacts:
        if i.mass/i.mass_true >= 2:
            min_mass.append(i)
    min_mass = sorted(min_mass, key=lambda x: x.mass_true)
    return render(request, 'notification.html', {'min_srok': min_srok, 'min_mass': min_mass})
