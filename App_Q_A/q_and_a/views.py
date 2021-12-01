from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Pregunta, Respuesta
from .forms import PreguntaForm, RespuestaForm

# Vista de listado de preguntas
class ListaPreguntas(generic.ListView):
    # Obtiene lista de preguntas
    # queryset = Pregunta.objects.order_by('-fecha_publicacion')
    # Indica la plantilla a utilizar
    template_name = 'index.html'

    # Definición para obtener preguntas
    def get_queryset(self):
        # Obtiene tema de busqueda en la peticion
        tema = self.request.GET.get('tema', '')
        if(tema != ''):
            query = Q(titulo__icontains=tema)
            queryset = Pregunta.objects.filter(query).order_by('-fecha_publicacion')
        else:
            queryset = Pregunta.objects.order_by('-fecha_publicacion')
        return queryset

# Vista para acceder a los detalles de una pregunta
class DetallesPregunta(generic.DetailView):
    model = Pregunta
    template_name = 'detalles_pregunta.html'

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('preguntas:login')

# Vista para inicio de sesión
def login_view(request):
    # Valida que se haga una petción POST
    if request.method == "POST":
        # Recupera los datos del formulario
        form = AuthenticationForm(request, request.POST)
        # Verifica si el contenido es válido
        if form.is_valid():
            # Obtiene datos del usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Autentica al usuario
            user = authenticate(username=username, password=password)
            # Verifica si la autenticación fue correcta
            if user is not None:
                # Liga el usuario autenticado con la sesión
                login(request, user)
                return redirect('preguntas:home')
            else:
                messages.error(request, "Datos de usuario incorrectos")
        else:
            messages.error(request, "Datos de usuario incorrectos")
    form = AuthenticationForm()
    return render(request, 'login.html', {"login_form": form})

# Vista con el formulario de pregunta
def pregunta_form(request):
    # Valida si es un usuario sin autenticar
    if request.user.is_anonymous:
        # Usuarios no autenticados son redirigidos a página de login
        return redirect('preguntas:login')

    form = PreguntaForm
    # Valida que se hace una petición POST con AJAX
    if request.method == 'POST' and request.is_ajax():
        # Recupera información del formulario
        form  = PreguntaForm(request.POST)
        # Verifica que la información sea valida
        if form.is_valid():
            # Obtiene datos de la petición
            titulo = form.cleaned_data['titulo']
            # Guarda los datos recibidos en un objeto pero no en la BD
            pregunta = form.save(commit=False)
            # Añade los campos faltantes
            pregunta.fecha_publicacion = timezone.now()
            pregunta.autor = request.user
            # Se confirman los cambios en la BD
            pregunta.save()
            # Se devuelve un JSON con resultado exitoso
            return JsonResponse({"valor": titulo}, status=200)
        else:
            # Obtiene errores en formato JSON
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, 'formulario_pregunta.html', {"form": form})

# Vista con el formulario de la respuesta
def respuesta_form(request, pk):
    # Valida si es un usuario sin autenticar
    if request.user.is_anonymous:
        # Usuarios no autenticados son redirigidos a página de login
        return redirect('preguntas:login')

    # Obtiene la pregunta que se responderá
    pregunta = get_object_or_404(Pregunta, pk=pk)
    form = RespuestaForm

    # Valida que se hace una petición POST con AJAX
    if request.method == 'POST' and request.is_ajax():
        # Se obtienen datos de la solicitud POST
        form = RespuestaForm(request.POST)
        # Verifica que la información del formulario es válida
        if form.is_valid():
            # Guarda contenido del formulario
            respuesta = form.save(commit=False)
            # Completa los campos faltantes
            respuesta.fecha_respuesta = timezone.now()
            respuesta.pregunta = pregunta
            respuesta.status = 0
            # Confirma los cambios
            respuesta.save()
            # Devuelve repuesta JSON exitosa con id de la pregunta
            return JsonResponse({"valor": pk}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, 'formulario_respuesta.html',
        {"form": form, "pregunta": pregunta})
