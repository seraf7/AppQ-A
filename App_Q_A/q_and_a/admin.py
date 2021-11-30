from django.contrib import admin
from .models import Pregunta, Respuesta

# Clase para definir detalles vistos en el sitio de administración
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'fecha_publicacion', 'titulo')
    search_fields = ['titulo', 'detalle']

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'fecha_respuesta', 'contenido')
    list_filter = ('status', )

# Se añaden los modelos al sitio de administración
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
