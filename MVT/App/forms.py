from django import forms


class Familiares(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    