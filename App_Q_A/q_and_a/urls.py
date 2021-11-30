from . import views
from django.urls import path

app_name = 'preguntas'

# Se especifican las URL de la aplicación
urlpatterns = [
    path('', views.ListaPreguntas.as_view(), name='home'),
    # Acceso mediante la PK de la pregunta
    path('<int:pk>/', views.DetallesPregunta.as_view(), name='detalles_pregunta'),
]
