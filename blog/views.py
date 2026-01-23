from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post
from .forms import BuscarPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.decorators import login_required

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

class PostListView(ListView):
    model = Post
    template_name = "blog/pages_list.html"
    context_object_name = "posts"
    ordering = ["-fecha"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/page_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/page_form.html"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "categoria"]
    success_url = reverse_lazy("pages_list")

    def form_valid(self, form):
        # setea autor automáticamente con el usuario logueado
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/page_form.html"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "categoria"]
    success_url = reverse_lazy("pages_list")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/page_confirm_delete.html"
    success_url = reverse_lazy("pages_list")

@login_required
def about(request):
    return render(request, "blog/about.html")