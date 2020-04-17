from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('usuario/', views.usuario_list),
    path('oficina/', views.oficina_list),
    path('oficinacreate/', csrf_exempt(views.create_oficina), name='oficinaCreate'),
    path('usuariocreate/', csrf_exempt(views.create_user), name='usuarioCreate'),

]