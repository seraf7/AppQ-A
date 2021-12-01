from django import forms
from .models import Pregunta

# Clase para definir el formulario de una pregunta
class PreguntaForm(forms.ModelForm):
    class Meta:
        # Indica el modelo a utilizar
        model = Pregunta
        # Indica los campos del formulario
        fields = ('titulo', 'detalle')
