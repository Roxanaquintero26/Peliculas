from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class InicioView(TemplateView):
    template_name = "index.html"


# vistas de Peliculas
class PeliculaView(TemplateView): 
    template_name = "pelicula.html"
     