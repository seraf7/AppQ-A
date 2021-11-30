from django.shortcuts import render
from django.views import generic
from .models import Pregunta, Respuesta

# Vista de listado de preguntas
class ListaPreguntas(generic.ListView):
    # Obtiene lista de preguntas
    queryset = Pregunta.objects.order_by('-fecha_publicacion')
    # Indica la plantilla a utilizar
    template_name = 'index.html'

# Vista para acceder a los detalles de una pregunta
class DetallesPregunta(generic.DetailView):
    model = Pregunta
    template_name = 'detalles_pregunta.html'
