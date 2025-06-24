from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('details/<int:id>/', views.details, name='details'),
]

