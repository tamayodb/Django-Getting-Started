from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:id>/', views.details, name='details'),
]

