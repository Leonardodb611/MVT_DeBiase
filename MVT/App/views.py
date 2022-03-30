from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from App.forms import *

# Create your views here.

def inicio(request):
    return render (request, "App/inicio.html")

def familia(request):
    
    cont_familia = Familia.objects.all()

    if request.method == "POST":
        miFormulario = Familiares(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            familiar = Familia (nombre = informacion["nombre"],apellido = informacion["apellido"],dni = informacion["dni"])
            familiar.save()
            return render(request, "App/Gracias.html")


    
    else:
        miFormulario = Familiares()
    
        return render (request, "App/inicio.html", {"miFormulario":miFormulario, "cont_familia":cont_familia})

    return  render(request, "App/inicio.html", {"cont_familia":cont_familia})
        

