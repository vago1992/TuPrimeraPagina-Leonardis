from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post
from .forms import BuscarPostForm

def inicio(request):
    return render(request, "blog/inicio.html")

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AutorForm()
    return render(request, "blog/form.html", {"form": form, "titulo": "Crear Autor"})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = CategoriaForm()
    return render(request, "blog/form.html", {"form": form, "titulo": "Crear Categoría"})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = PostForm()
    return render(request, "blog/form.html", {"form": form, "titulo": "Crear Post"})

def buscar_post(request):
    form = BuscarPostForm(request.GET)
    resultados = []

    if form.is_valid():
        titulo = form.cleaned_data.get("titulo")
        if titulo:
            resultados = Post.objects.filter(titulo__icontains=titulo)

    return render(request, "blog/buscar_post.html", {"form": form, "resultados": resultados})