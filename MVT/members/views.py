from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
