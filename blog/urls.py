from django.urls import path
from .views import inicio, crear_autor, crear_categoria, crear_post, buscar_post, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, about



urlpatterns = [

    path("", inicio, name="inicio"),
    path("autor/nuevo/", crear_autor, name="crear_autor"),
    path("categoria/nueva/", crear_categoria, name="crear_categoria"),
    path("post/nuevo/", crear_post, name="crear_post"),
    path("buscar/", buscar_post, name="buscar_post"),
    path("pages/", PostListView.as_view(), name="pages_list"),
    path("pages/<int:pk>/", PostDetailView.as_view(), name="page_detail"),
    path("pages/create/", PostCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/update/", PostUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/delete/", PostDeleteView.as_view(), name="page_delete"),
    path("about/", about, name="about")
]