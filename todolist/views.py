from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return HttpResponse ("This is my list")
