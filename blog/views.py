from django.shortcuts import render, get_object_or_404, redirect
from .forms import AutorForm, PostForm, CategoriaForm
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Autor'})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Categoría'})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Post'})

def buscar_post(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'query': query})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})