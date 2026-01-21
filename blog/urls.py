from django.urls import path
from .views import inicio, crear_autor, crear_categoria, crear_post
from .views import buscar_post


urlpatterns = [
    path("", inicio, name="inicio"),
    path("autor/nuevo/", crear_autor, name="crear_autor"),
    path("categoria/nueva/", crear_categoria, name="crear_categoria"),
    path("post/nuevo/", crear_post, name="crear_post"),
    path("buscar/", buscar_post, name="buscar_post")
]