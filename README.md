# TuPrimeraPaginaCamacaro ✨

Este es un proyecto básico creado con Django para aprender cómo desarrollar una página web que permite gestionar autores, categorías y publicaciones de un blog.

---

## Características

- Registro y visualización de autores.
- Clasificación de publicaciones por categorías.
- Creación, búsqueda y listado de posts.
- Interfaz estilizada con CSS personalizado.
- Imagen de fondo decorativa y diseño centrado.

---

## Tecnologías utilizadas

- Python 3.x
- Django 4.x
- HTML5, CSS3
- VSCode
- SQLite

---
## Estructura del Proyecto

- Uso del patrón **MVT**
- App principal: `blog`
- Modelos: `Autor`, `Categoria`, `Post`
- Formularios de creación para cada modelo
- Buscador de posts por título
- Navegación completa con enlaces visibles
- Herencia de plantillas con `base.html`

## Funcionalidades

- Crear autores: `/autor/`
- Crear categorías: `/categoria/`
- Crear posts: `/post/`
- Buscar posts: `/buscar/`
- Ver detalles de post: `/post/<id>/`

## Buscador

El buscador permite filtrar los posts por coincidencia parcial en el título. Desde los resultados puedes acceder al detalle del post.

## Acceso al Panel de Administración

Puedes acceder al panel de administración desde:
http://127.0.0.1:8000/admin/

---
### Credenciales del Superusuario

- **Usuario:** `yoli_`
- **Contraseña:** `yoliyoli2122`

> *Puedes agregar y editar registros de `Autor`, `Categoria` y `Post` desde el panel admin.*

---

## Cómo ejecutar el proyecto

1. Clona el repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/tu_usuario/TuPrimeraPaginaCamacaro.git
   cd TuPrimeraPaginaCamacaro

---

