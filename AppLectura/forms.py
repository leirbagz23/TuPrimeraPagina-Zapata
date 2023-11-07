from django import forms
#Formularios creados para hacer el registro de objetos en cada modelo en el sitio web.
class LeidosFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
class LeyendoFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
class PorLeerFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
