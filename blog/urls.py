from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_posts, name='buscar_posts'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
]
