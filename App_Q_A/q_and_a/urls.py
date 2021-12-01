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
    # Página para cerrar sesión
    path('logout', views.logout_view, name='logout'),
    # Página de formulario de preguntas
    path('preguntar/', views.pregunta_form, name='pregunta_form'),
    # Página para crear respuestas
    path('<int:pk>/responder/', views.respuesta_form, name='respuesta_form'),
]
