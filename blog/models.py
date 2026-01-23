from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)              # CharField 1
    subtitulo = models.CharField(max_length=200)           # CharField 2 (nuevo)
    contenido = RichTextField()                            # ckeditor (antes TextField)
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)  # imagen
    fecha = models.DateTimeField(auto_now_add=True)        # fecha (si ya tenías DateField, también vale)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

def __str__(self):
    return self.titulo