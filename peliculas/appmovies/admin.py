from django.contrib import admin
 
from .models import TipoPelicula,Pelicula,Favorito,Historial,PerfilUsuario
# Register your models here.

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipoPelicula', 'poster', 'sipnosis', 'duracion',
                    'clasificacion', 'estado')

    ordering = ('tipoPelicula',)
    search_fields = ('tipoPelicula', 'clasificacion', 'titulo')
    list_filter = (
        'tipoPelicula__descripcion',
        'estado',
    )

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'usuario', 'fecha', 'estado')
    ordering = ('pelicula',)
    search_fields = ('pelicula', 'usuario','estado')
    list_filter = (
        'pelicula',
        'estado',
    )

class HistorialAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'usuario', 'fecha', 'estado')
    ordering = ('pelicula',)
    search_fields = ('pelicula', 'usuario','estado')
    list_filter = (
        'pelicula',
        'estado',
    )


class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'direccion','telefono','metodo_pago','preferencias', 'estado')
    ordering = ('usuario',)
    search_fields = ('usuario','metodo_pago','estado')
    list_filter = (
        'usuario',
        'estado',
    )

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Favorito, FavoritoAdmin)
admin.site.register(Historial, HistorialAdmin)
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
admin.site.register(TipoPelicula)





