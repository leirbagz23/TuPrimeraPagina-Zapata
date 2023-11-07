from django.shortcuts import render
from AppLectura.forms import LeidosFormulario,PorLeerFormulario,LeyendoFormulario
from AppLectura.models import Leidos,Por_Leer,Leyendo
from django.http import HttpResponse
# Create your views here.
#Pagina de inicio que muestra las bases de datos de los modelos de la App AppLectura
def home(request):
    leidos=Leidos.objects.all
    leyendo=Leyendo.objects.all
    por_leer=Por_Leer.objects.all
    return render(request,'home.html',{'leidos':leidos,'leyendo':leyendo,'por_leer':por_leer})
#Pagina que contiene el formulario para registrar objetos en el modelo por_leer
def por_leer(request):
    if request.method=="POST":
        por_leer_formulario=PorLeerFormulario(request.POST)
        print(por_leer_formulario)
        if por_leer_formulario.is_valid():
            informacion=por_leer_formulario.cleaned_data
            por_leer=Por_Leer(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            por_leer.save()
            return render(request,'porleer.html')
    else:
        por_leer_formulario=Por_Leer()
        return render(request,'porleer.html',{"por_leer_formulario":por_leer_formulario})
#Pagina que contiene el formulario para registrar objetos en el modelo leidos
def leidos(request):
    if request.method=="POST":
        leidos_formulario=LeidosFormulario(request.POST)
        print(leidos_formulario)
        if leidos_formulario.is_valid():
            informacion=leidos_formulario.cleaned_data
            leidos=Leidos(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            leidos.save()
            return render(request,'leidos.html')
    else:
        leidos_formulario=Leidos()
        return render(request,'leidos.html',{"leidos_formulario":leidos_formulario})
#Pagina que contiene el formulario para registrar objetos en el modelo leyendo
def leyendo(request):
    if request.method=="POST":
        leyendo_formulario=LeyendoFormulario(request.POST)
        print(leyendo_formulario)
        if leyendo_formulario.is_valid():
            informacion=leyendo_formulario.cleaned_data
            leyendo=Leyendo(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            leyendo.save()
            return render(request,'leyendo.html')
    else:
        leyendo_formulario=Leyendo()
        return render(request,'leyendo.html',{"leyendo_formulario":leyendo_formulario})
#Pagina que contiene el formulario para realizar busquedas en las bases de datos, pudiendo buscar por autor, por titulo de libro o por año de publicación
def busqueda(request):
    return render(request,'busqueda.html')
#Pagina que muestra los resultados obtenidos de acuerdo a la búsqueda realizada en la página busqueda
def resultado_busqueda(request):
    if request.GET["titulo"]:
        busqueda=request.GET["titulo"]
        resultado1=Leidos.objects.filter(titulo__icontains=busqueda)
        resultado2=Leyendo.objects.filter(titulo__icontains=busqueda)
        resultado3=Por_Leer.objects.filter(titulo__icontains=busqueda)
        return render(request,'resultado.html',{'busqueda':busqueda,'resultado1':resultado1,'resultado2':resultado2,'resultado3':resultado3})
    elif request.GET["autor"]:
        busqueda=request.GET["autor"]
        resultado1=Leidos.objects.filter(autor__icontains=busqueda)
        resultado2=Leyendo.objects.filter(autor__icontains=busqueda)
        resultado3=Por_Leer.objects.filter(autor__icontains=busqueda)
        return render(request,'resultado.html',{'busqueda':busqueda,'resultado1':resultado1,'resultado2':resultado2,'resultado3':resultado3})
    elif request.GET["año_publicacion"]:
        busqueda=request.GET["año_publicacion"]
        resultado1=Leidos.objects.filter(año_publicacion__icontains=busqueda)
        resultado2=Leyendo.objects.filter(año_publicacion__icontains=busqueda)
        resultado3=Por_Leer.objects.filter(año_publicacion__icontains=busqueda)
        return render(request,'resultado.html',{'busqueda':busqueda,'resultado1':resultado1,'resultado2':resultado2,'resultado3':resultado3})
    else:
        return HttpResponse('No se realizó ninguna búsqueda')