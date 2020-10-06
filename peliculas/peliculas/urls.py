"""peliculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from appmovies.views import InicioUsuarioView,HistorialInicioView,InicioPeliculaView,InicioFavoritoView,LoginView,InicioView, PeliculaView, CrearPeliculaView, EditarPeliculaView, EliminarPeliculaView,FavoritoView,CrearFavoritoView,EditarFavoritoView,EliminarFavoritoView,HistorialView, CrearHistorialView, EditarHistorialView, EliminarHistorialView,PerfilUsuarioView,CrearPerfilUsuarioView,EditarPerfilUsuarioView,EliminarPerfilUsuarioView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    


    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),

    path('peliculas/', InicioPeliculaView.as_view(), name='inicio_peliculas'),
    path('pelicula/', PeliculaView.as_view(), name='pelicula'),

    path('crear_pelicula/', CrearPeliculaView.as_view(), name='crear_pelicula'),
    path('editar_pelicula/<int:pk>/',
         EditarPeliculaView.as_view(), name='editar_pelicula'),
    path('eliminar_pelicula/<int:pk>/',
         EliminarPeliculaView.as_view(), name='eliminar_pelicula'),
    
    path('favoritos/', InicioFavoritoView.as_view(), name='inicio_favorito'),
    path('favorito/', FavoritoView.as_view(), name='favorito'),
    path('crear_favorito/', CrearFavoritoView.as_view(), name='crear_favorito'),
    path('editar_favorito/<int:pk>/',
         EditarFavoritoView.as_view(), name='editar_favorito'),
    path('eliminar_favorito/<int:pk>/',
         EliminarFavoritoView.as_view(), name='eliminar_favorito'),


    path('historiales/', HistorialInicioView.as_view(), name='inicio_historial'),
    path('historial/', HistorialView.as_view(), name='historial'),
    path('crear_historial/', CrearHistorialView.as_view(), name='crear_historial'),
    path('editar_historial/<int:pk>/',
         EditarHistorialView.as_view(), name='editar_historial'),
    path('eliminar_historial/<int:pk>/',
         EliminarHistorialView.as_view(), name='eliminar_historial'),

     
    path('usuarios/', InicioUsuarioView.as_view(), name='inicio_usuario'),
    path('usuario/', PerfilUsuarioView.as_view(), name='usuario'),
    path('crear_usuario/', CrearPerfilUsuarioView.as_view(), name='crear_usuario'),
    path('editar_usuario/<int:pk>/',
         EditarPerfilUsuarioView.as_view(), name='editar_usuario'),
    path('eliminar_usuariol/<int:pk>/',
         EliminarPerfilUsuarioView.as_view(), name='eliminar_usuario'),
]


# Configuracion de las imagenes para en django
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
