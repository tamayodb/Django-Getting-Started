from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Members

def members (request):
    members = Members.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context, request))

def details (request, id):
    details = Members.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'details' : details,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())