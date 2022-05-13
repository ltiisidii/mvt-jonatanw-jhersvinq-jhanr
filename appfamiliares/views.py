from django.shortcuts import render
from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse
from appfamiliares.models import Familiar


def mis_familiares(request):
    template = loader.get_template('index.html')
    documento = template.render({
        'familiares': Familiar.objects.all()
    })
    return HttpResponse(documento)