from . import views
from django.urls import path

app_name = 'preguntas'

# Se especifican las URL de la aplicación
urlpatterns = [
    # Listado general de preguntas
    path('', views.ListaPreguntas.as_view(), name='home'),
    # Listado de preguntas por búsqueda
    path('buscar/', views.ListaPreguntas.as_view(), name='buscar'),
    # Acceso mediante la PK de la pregunta
    path('<int:pk>/', views.DetallesPregunta.as_view(), name='detalles'),
    # Página de inicio de sesión
    path('login', views.login_view, name='login'),
]
