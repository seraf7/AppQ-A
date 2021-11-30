from django.db import models
from django.contrib.auth.models import User

# Clase para modelar una pregunta
class Pregunta(models.Model):
    titulo = models.CharField(max_length=200)
    detalle = models.TextField()
    fecha_publicacion = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # Clase para ordenar preguntas por la más reciente
    class Meta:
        ordering = ['-fecha_publicacion']

    # Representa objeto como cadena
    def __str__(self):
        return self.titulo

CORRECTA = ((0, "Respuesta sin validar"), (1, "Respuesta correcta"))

# Clase para modelar una respuesta
class Respuesta(models.Model):
    contenido = models.TextField()
    fecha_respuesta = models.DateTimeField()
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    status = models.IntegerField(choices=CORRECTA, default=0)

    # Representación como cadena
    def __str__(self):
        return self.contenido
