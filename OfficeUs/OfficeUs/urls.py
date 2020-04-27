from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', views.index),
    path('', include('usuario.urls')),
    path('oficinas/', include('oficina.urls')),
]
