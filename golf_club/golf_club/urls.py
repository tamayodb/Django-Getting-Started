from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('members/', permanent=False)),
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]
