from django import forms
from .models import Pelicula, Favorito, Historial,PerfilUsuario


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'tipoPelicula', 'poster', 'sipnosis', 'duracion',
                  'clasificacion', 'trailer', 'estado')
        label = {
            'titulo': 'Titulo',
            'tipoPelicula': 'Tipo de Pelicula',
            'poster': 'Poster',
            'sipnosis': 'Sipnosis',
            'duracion': 'Duracion',
            'clasificacion': 'Clasificacion',
            'trailer': 'Trailer',
            'estado': 'Estado'
        }

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipoPelicula': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'poster': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sipnosis': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'clasificacion': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class FavoritoForm(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = ('pelicula','usuario','fecha','estado')
        label = {
            'pelicula': 'Pelicula',
            'usuario': 'Usuario',
            'fecha': 'Fecha',
            'estado': 'Estado',
        }
        widgets = {
            'pelicula': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ('pelicula','usuario','fecha','estado')
        label = {
            'pelicula': 'Pelicula',
            'usuario': 'Usuario',
            'fecha': 'Fecha',
            'estado': 'Estado',
            
        }

        widgets = {
            'pelicula': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ('usuario', 'direccion','telefono','metodo_pago','preferencias', 'estado')
        label = {
            'usuario': 'Usuario',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'metodo_pago': 'MetodoPago',
            'preferencias': 'Preferencias',
            'estado': 'Estado',
            
        }

        widgets = {
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'metodo_pago': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'preferencias': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
