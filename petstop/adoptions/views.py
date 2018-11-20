from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template

from django.http import *

from .models import Pet
def home(request):
   
    try:
        pets = Pet.objects.all()
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
 
    t = get_template("home.html")
    html = t.render({'pets': pets})

    return HttpResponse(html)
