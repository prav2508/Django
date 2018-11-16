from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template

from django.http import *

from .models import Pet
def home(request):
    pets = Pet.objects.all()
    t = get_template("home.html")
    html = t.render({'pets': pets})

    return HttpResponse(html)
