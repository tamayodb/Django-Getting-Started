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

def testing(request):
   dummy_data = Members.objects.all()
   template = loader.get_template('template.html')
   context = {
      'basic_details': {'firstname': 'Samantha', 'phone': '6398237462537', 'joined_date': '26-05-2025'},
      'dummy_data': dummy_data,
   }
   return HttpResponse(template.render(context, request))
