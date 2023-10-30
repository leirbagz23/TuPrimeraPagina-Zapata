from django.shortcuts import render
from AppLectura.forms import LeidosFormulario,PorLeerFormulario,LeyendoFormulario
from AppLectura.models import Leidos,Por_Leer,Leyendo
# Create your views here.
def home(request):
    return render(request,'home.html')
def por_leer(request):
    if request.method=="POST":
        por_leer_formulario=PorLeerFormulario(request.POST)
        print(por_leer_formulario)
        if por_leer_formulario.is_valid():
            informacion=por_leer_formulario.cleaned_data
            por_leer=PorLeerFormulario(informacion["titulo"],informacion["autor"],informacion["año_publicacion"])
            por_leer.save()
            return render(request,'home.html')
    else:
        por_leer_formulario=Por_Leer()
        return render(request,'porleer.html',{"por_leer_formulario":por_leer_formulario})
def leidos(request):
    if request.method=="POST":
        leidos_formulario=LeidosFormulario(request.POST)
        print(leidos_formulario)
        if leidos_formulario.is_valid():
            informacion=leidos_formulario.cleaned_data
            leidos=Leidos(informacion["titulo"],informacion["autor"],informacion["año_publicacion"])
            leidos.save()
            return render(request,'home.html')
    else:
        leidos_formulario=Leidos()
        return render(request,'leidos.html',{"leidos_formulario":leidos_formulario})
def leyendo(request):
    if request.method=="POST":
        leyendo_formulario=LeyendoFormulario(request.POST)
        print(leyendo_formulario)
        if leyendo_formulario.is_valid():
            informacion=leyendo_formulario.cleaned_data
            leyendo=Leyendo(informacion["titulo"],informacion["autor"],informacion["año_publicacion"])
            leyendo.save()
            return render(request,'home.html')
    else:
        leyendo_formulario=Leyendo()
        return render(request,'leyendo.html',{"leyendo_formulario":leyendo_formulario})
def busqueda(request):
    return render(request,'busqueda.html') 