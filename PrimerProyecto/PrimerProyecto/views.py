from multiprocessing import context
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

#crear una vista en django: con una fucnion

#vista: es para devolvernos una respuestas

def saludo(request):
    return HttpResponse("HOLA ESTA ES NUESTRA PRIMERA PAGINA WEB") #devolvernos la respuesta

#debemos solictar una url que nos mostrara la vista
#debemos enlazar un enlace para que muestre nuestra vista

def Name(request):
    return HttpResponse("MI NOMBRE ES ANDRES Y ESTA ES MI PAGINA EN DJANGO")


def Despedida(request):
    return HttpResponse("HASTA LUEGO AMIGO")



def OtroSaludo(request):
    return HttpResponse("ENVIANDO OTRO SALUDO")
    

def Curso(request):
    return HttpResponse("ESTOY TOMANDO EL CURSO DE DESARROLLO DE SOFTWARE ")

def HoraFecha(request):
    fecha_actual = datetime.datetime.now()

    FormatoHTML = """<html>
    <body>
    <h1> Fecha y Hora actual: %s #marcador de posicion: 
    </h1>
    </body>
    </html> 
    """  % fecha_actual
    #%h #marcador de posicion: 

   
    return HttpResponse(FormatoHTML)

def Años(request):
    año = 2070
    nacimiento = 1999

    futuro = año - nacimiento

    return HttpResponse(futuro)

def MayorEdad(request, edad):
    if edad>=18:
        return HttpResponse("es mayor de edad")
    else:
        return HttpResponse("es menor de edad")

def ContenidoHTML(request, nombre, edad):
    contenido = """<html>
    <body>
    <p> nombre: %s / edad: %s</p>
    </body>
    </html>
    """ %(nombre,edad) #codigo HTML creaod en una vista, Plantilla htm en una vista
    return HttpResponse(contenido)

class Persona(object):
    def __init__(self, curso, universidad):
        self.curso=curso
        self.universidad=universidad #instancimos la clase Persona en la vista y la gregamos a la plantilla


def Plantilla(request): #vista capaz de cagar plantilla
    #abrimos el documento que contiene la plantilla

    nombre1 = "andres"
    apellido = "silvera"
    Andres = Persona("Python", "UNAL")


    #plantillaexterna = open(r"C:\Users\jose\Desktop\Proyecto Django\PrimerProyecto\PrimerProyecto\Mis Plantillas\Plantillas.html")
   #cargar el documento en una variable de tipo template
    #template = Template(plantillaexterna.read())
    #plantilla_Externa = loader.get_template("Plantillas.html")
    
    #cerrrar el documento externo que hemos abierto
    #plantillaexterna.close()
    #contexto = Context({"nombre_persona": nombre1, "apellido_persona": apellido, "curso1": Andres.curso, "universidad1": Andres.universidad, "listas":["Django", "Views","condicionales","bulces for y while", "clases"]}) #agregar variables o funciones a la plantilla a traves de un diccionario
    #documento = plantilla_Externa.render({"nombre_persona": nombre1, "apellido_persona": apellido, "curso1": Andres.curso, "universidad1": Andres.universidad, "listas":["Django", "Views","condicionales","bulces for y while", "clases"]})

    return render(request, "Plantillas.html", {"nombre_persona": nombre1, "apellido_persona": apellido, "curso1": Andres.curso, "universidad1": Andres.universidad, "listas":["Django", "Views","condicionales","bulces for y while", "clases"]})