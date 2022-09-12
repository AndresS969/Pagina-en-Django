from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def mostrar(request):
    return render(request, "index.html")

def buscar(request):
    anal = request.GET["prd"]
    anal2 = request.GET["contraseña"]
    x = "Usuario: {}, Contraseña: {}".format(anal, anal2)
    return HttpResponse(x)



def suma(request):
    numero = int(request.GET["numero1"])
    numero_1 = int(request.GET["numero2"])

    user_password = f"La suma es: {numero+numero_1}"

    return HttpResponse(user_password)

def listado(request):
    lista=[]
    y = request.GET["listas"].split(",")


    no = f"frameworks de mi lista: {y}"
    return HttpResponse(no)


def servidor(request):
    
    return render(request, "servidor.html")


def Persona(request):
    return render(request, "condicion.html")



def calcular(request):
    name = request.GET["name1"]
    age = int(request.GET["edad1"])
    information = f"nombre: {name}, edad: {age}"
    if age>=18:
        return HttpResponse("es mayor de edad!")
    else:
        return HttpResponse(information)

def formulario_lsogin(request):
    return render(request, "formulario.html")


def user_password(request):
    len_user= request.GET["usuario"]
    
    if  request.GET["usuario"] and int(request.GET["contraseña"]):      
        url_screen = f"""My new user is: {request.GET["usuario"]}
                    #My password is: {int(request.GET["contraseña"])}"""
        if len(len_user)>8:
            url_screen = "texto demasiado largo!"
        return HttpResponse(url_screen)
         
    else:

        return HttpResponse("Debe ingresar los datos solicitados!")


def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html")
        
    return render(request, "formulario_contacto.html")

