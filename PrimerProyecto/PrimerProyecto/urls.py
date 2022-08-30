
from django.contrib import admin
from django.urls import path



from PrimerProyecto.views import saludo #importmaos la funcion
from PrimerProyecto.views import Name, Despedida
from PrimerProyecto.views import OtroSaludo, Curso
from PrimerProyecto.views import HoraFecha
from PrimerProyecto.views import Años, MayorEdad, ContenidoHTML,Plantilla, hija


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #enlazamos nuestra vista a la url
    path('Name/', Name),
    path('Despedida/', Despedida),
    path('OtroSaludo/', OtroSaludo),
    path('Curso/', Curso),
    path('HoraFecha/', HoraFecha),
    path('Años/', Años),
    path('MayorEdad/<int:edad>', MayorEdad), #url con parametros
    
    path('ContenidoHTML/<nombre>/<int:edad>',ContenidoHTML), #usamos barra invertida para separar parametros
    path('Plantilla/', Plantilla),
    path('anal/', hija),
]
