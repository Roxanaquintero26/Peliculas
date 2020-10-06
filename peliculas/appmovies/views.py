from .models import Pelicula, Favorito, Historial,PerfilUsuario
from .forms import PeliculaForm, FavoritoForm, HistorialForm, PerfilUsuarioForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
 
# Create your views here.

class LoginView(TemplateView):
    template_name="login.html"

class CatalogoView(TemplateView):
    template_name="index.html"

class InicioView(TemplateView):
    template_name = "index.html"




# vistas de Peliculas
class InicioPeliculaView(TemplateView):
    template_name = "index.html"


class PeliculaView(ListView):
    model = Pelicula
    template_name = "pelicula.html"
    context_object_name = "peliculas"
    #queryset = Pelicula.objects.filter(titulo="avenger")


class CrearPeliculaView(CreateView):
    model = Pelicula
    template_name = "crear_pelicula.html"
    form_class = PeliculaForm
    success_url = reverse_lazy('pelicula')


class EditarPeliculaView(UpdateView):
    model = Pelicula
    template_name = "crear_pelicula.html"
    form_class = PeliculaForm
    success_url = reverse_lazy('pelicula')


class EliminarPeliculaView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        pelicula = Pelicula.objects.get(id=pk)
        pelicula.delete()
        # object.estado = False
        # object.save()
        return redirect('pelicula')






# vistas de Favoritos
class InicioFavoritoView(TemplateView):
    template_name = "indexFavorito.html"


class FavoritoView(ListView):
    model = Favorito
    template_name = "favorito.html"
    context_object_name = "favoritos"

class CrearFavoritoView(CreateView):
    model = Favorito
    template_name = "crear_favorito.html"
    form_class = FavoritoForm
    success_url = reverse_lazy('favorito')

class EditarFavoritoView(UpdateView):
    model = Favorito
    template_name = "crear_favorito.html"
    form_class = FavoritoForm
    success_url = reverse_lazy('favorito')

class EliminarFavoritoView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        favorito = Favorito.objects.get(id=pk)
        favorito.delete()
        # object.estado = False
        # object.save()
        return redirect('favorito')


#Vistas del Historial
class HistorialInicioView(TemplateView):
    template_name = "indexHistorial.html"

class HistorialView(ListView):
    model = Historial
    template_name = "historial.html"
    context_object_name = "historiales"

class CrearHistorialView(CreateView):
    model = Historial
    template_name = "crear_historial.html"
    form_class = HistorialForm
    success_url = reverse_lazy('historial')


class EditarHistorialView(UpdateView):
    model = Historial
    template_name = "crear_historial.html"
    form_class = HistorialForm
    success_url = reverse_lazy('historial')


class EliminarHistorialView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        historial = Historial.objects.get(id=pk)
        historial.delete()
        # object.estado = False
        # object.save()
        return redirect('historial')


#Vistas del Perfil de usuario

class InicioUsuarioView(TemplateView):
    template_name = "indexUsuario.html"



class PerfilUsuarioView(ListView):
    model = PerfilUsuario
    template_name = "usuario.html"
    context_object_name = "usuarios"

class CrearPerfilUsuarioView(CreateView):
    model = PerfilUsuario
    template_name = "crear_usuario.html"
    form_class = PerfilUsuarioForm
    success_url = reverse_lazy('usuario')


class EditarPerfilUsuarioView(UpdateView):
    model = PerfilUsuario
    template_name = "crear_usuariol.html"
    form_class = PerfilUsuarioForm
    success_url = reverse_lazy('usuario')


class EliminarPerfilUsuarioView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        usuario = PerfilUsuario.objects.get(id=pk)
        usuario.delete()
        # object.estado = False
        # object.save()
        return redirect('usuario')

