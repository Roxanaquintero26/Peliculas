from django.db import models

from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class TipoPelicula(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha Creacion',auto_now=False,auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Fecha Modificacion',auto_now=True,auto_now_add=False)
    fecha_eliminacion = models.DateTimeField('Fecha Eliminacion',auto_now=True,auto_now_add=False)
    
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ["descripcion"]
        verbose_name = "Tipo de Pelcula"
        verbose_name_plural = "Tipos de Pelculas"

    def __str__(self):
        return "{}".format(self.descripcion)


class Pelicula(models.Model):
    clasificacion_pelicula = (
        ('T', 'Todo Publico'), ('N', 'Niños menores de 12 años'), ('A', 'Mayores de 18 años'))

    titulo = models.CharField('Titulo Pelicula', max_length=100)

    tipoPelicula = models.ForeignKey(TipoPelicula, on_delete=models.PROTECT)

    poster = models.ImageField('Poster Pelicula',
    upload_to='poster/', blank=True, null=True)

    sipnosis = models.TextField('Sipnosis')

    duracion = models.DecimalField(
        'Duracion pelicula', decimal_places=2, max_digits=10)

    clasificacion = models.CharField(
        'Clasificacion Pelicula', choices=clasificacion_pelicula, max_length=1, default='T')

    trailer = models.URLField('Trailer Pelicula', max_length=500)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Fecha Creacion',auto_now=False,auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Fecha Modificacion',auto_now=True,auto_now_add=False)
    fecha_eliminacion = models.DateTimeField('Fecha Eliminacion',auto_now=True,auto_now_add=False)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Pelcula"
        verbose_name_plural = "Pelculas"

    def __str__(self):
        return "{}".format(self.titulo)


class Favorito(models.Model):
    pass 

class Historial(models.Model):
    pass 

class PerfilUsuario(models.Model):
    pass

