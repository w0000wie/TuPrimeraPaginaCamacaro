from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'blog/home.html')

def autores(request):
    return render(request, 'blog/autores.html')

def categorias(request):
    return render(request, 'blog/categorias.html')

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def buscar_posts(request):
    query = request.GET.get('q')
    resultados = Post.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'blog/buscar.html', {'resultados': resultados})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})