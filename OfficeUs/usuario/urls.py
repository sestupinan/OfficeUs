from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('usuario/', views.usuario_list),
    path('usuariocreate/', views.usuario_create, name='usuario_create'),
    path('usuario/profile/<int:id>/<opcion>', views.usuario_profile,name='usuario_profile'),
]