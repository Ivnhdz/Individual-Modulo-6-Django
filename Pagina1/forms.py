from django import forms
from .models import Formulario

class MiFormulario(forms.ModelForm):
    cuerpo = forms.CharField(required = True)

    class Meta:
        model = Formulario
        fields = ["cuerpo"]