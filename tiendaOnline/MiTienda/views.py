from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from tiendaOnline.forms import Api_Validaion 
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail

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


def enviar(request):
    return render(request, "probando.html")


def request_answer(request):
    x = request.GET["username"]
    y = request.GET["userpassword"]

    if request.GET["username"] and int(request.GET["userpassword"]):
    
        show_infos = f"My Username is {x},and my password is {int(y)}"
        if len(x)>10:
            show_infos="ha sobrepasado ellimite de caracteres"
            
        return HttpResponse(show_infos)
    else:

        return HttpResponse("debe ingresar los datos!")
        
        
def Form_Api(request):
    if request.GET=="POST":
        mi_formulario = Api_Validaion(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data()
            send_mail(informacion["asunto"], informacion["mensaje"], informacion.get("email", ""),["afsilvera@mail.uniatlantico.edu.co"],)
            return render(request, "gracias.html")
    else:
        mi_formulario=Api_Validaion()
    return render(request, "formulario_API.html", {"form": mi_formulario})
