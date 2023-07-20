from django import forms
from .models import Formulario

class MiFormulario(forms.ModelForm):
    cuerpo = forms.CharField(required = True,
                            widget= forms.widgets.Textarea(
                                attrs={
                                    "placeholder": "Escribe el mensaje aca",
                                    "class": "textarea is-success is-medium"
                                }
                            )) 

    class Meta:
        model = Formulario
        fields = ["cuerpo"]