from django import forms
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
