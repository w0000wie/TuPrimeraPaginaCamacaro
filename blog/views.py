from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Autor'})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nueva Categoría'})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Post'})

def buscar_post(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})
