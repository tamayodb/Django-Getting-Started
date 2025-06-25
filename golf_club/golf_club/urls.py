from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from members import views 

urlpatterns = [
    path('', lambda request: redirect('main/', permanent=False)),
    path('main/', views.main, name='main'), 
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]