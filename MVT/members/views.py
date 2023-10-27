from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = User.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('index.html')
    user = request.user
    if request.user.is_authenticated:
        print(user.username + ' is logged in')
    context = {
        'user': user
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
