# TuPrimeraPagina+Leonardis

Proyecto Web desarrollado en Django siguiendo el patrón MVT.

## Descripción
La aplicación simula un blog simple donde se pueden crear autores, categorías y posts, y realizar búsquedas de posts por título.

## Funcionalidades

- Panel de administración de Django
- Herencia de templates HTML
- Modelos:
  - Autor
  - Categoria
  - Post
- Formularios para:
  - Crear Autor
  - Crear Categoria
  - Crear Post
- Formulario de búsqueda de Posts por título

## Orden para probar la aplicación

1. Clonar el repositorio
2. Crear entorno virtual:
py -m venv .venv

3. Activar entorno virtual:

..venv\Scripts\activate

4. Instalar dependencias:


py -m pip install django

5. Ejecutar migraciones:


py manage.py migrate

6. Crear superusuario:


py manage.py createsuperuser

7. Ejecutar el servidor:


py manage.py runserver

8. Acceder a:
- http://127.0.0.1:8000/ → sitio principal
- http://127.0.0.1:8000/admin/ → panel de administración

## Estructura del proyecto

- blog/ → app principal
- proyecto/ → configuración del proyecto
- templates/ → herencia de HTML