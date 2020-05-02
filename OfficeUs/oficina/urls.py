from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('get%<int:pagina>', views.get,name='get'),
    path('get/<keyword>%<int:pagina>', views.get_oficina_dado_keyword,name='get_oficina_dado_keyword'),
    path('get/<int:ide>', views.get_oficina_dado_id,name='get_oficina_dado_id'),
   #path('oficinacreate/', csrf_exempt(views.create_oficina), name='oficinaCreate'),

]