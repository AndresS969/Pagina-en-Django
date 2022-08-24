from django.http import HttpResponse
import datetime

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
