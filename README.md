# AppQ-A
Construcción de una aplicación de Questions &amp; Answers con funcionalidad básica al estilo StackOverflow.

## Pre-requisitos
Para poder ejecutar la aplicación, se requiere que el equipo se tenga instalado Python3, así como el framework Django y el módulo crispy-forms.

Para realizar la instalación de Django, usar el siguiente comando
```
pip3 install Django==3.2.6
```

Para realizar la instalación de crispy-forms, usar el siguiente comando
```
pip3 install django-crispy-forms
```

## Ejecución de la aplicación
Clonar el repositorio de GitHub en el destino elegido
```
git clone https://github.com/seraf7/AppQ-A.git
```
Moverse al directorio principal de la aplicación
```
cd AppQ-A/App_Q_A
```
Validar el proyecto de Django. Se debe obtener el mensaje *System check identified no issues (0 silenced)*
```
python3 manage.py check
```
Finalmente levantar el servidor
```
python3 manage.py runserver
```
Acceder a la aplicación mediante la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

De manera alternativa, se puede indicar un puerto y dirección IP específicos para levantar el servidor
```
python3 manage.py runserver <IP>:<puerto>
```

El usuario para realizar las pruebas de login es:
* username: usuario1
* password: algunusr
