from django.shortcuts import render
from .models import React
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "index.html")


def notification(request):
    reacts = React.objects.all()
    min_srok = sorted(reacts, key=lambda x: x.srok)[:2]
    min_mass = sorted(reacts, key=lambda x: x.mass)[:2]
    return render(request, 'notification.html', {'min_srok': min_srok, 'min_mass': min_mass})
