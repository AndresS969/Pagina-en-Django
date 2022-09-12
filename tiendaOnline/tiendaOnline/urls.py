
from django.contrib import admin
from django.urls import path
from MiTienda import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mostrar/', views.mostrar),
    path('buscar/', views.buscar),
    path('servidor/', views.servidor),
    path('Suma/', views.suma),
    path('listado/', views.listado),
    path('persona/', views.Persona),
    path('edad/', views.calcular),
    path('formulario/', views.formulario_lsogin),
    path('login/', views.user_password),
]
