from django import forms
from .models import Discoteca

class DiscotecaForm(forms.ModelForm):
    class Meta:
        model = Discoteca
        fields = ['dias','horario','nombre', 'direccion', 'descripcion', 'genero', 'servicio1','servicio2','servicio3', 'sucursales', 'ubicacion_latitud', 'ubicacion_longitud', 'red_social1', 'red_social2', 'red_social3', 'url_video1', 'url_video2']
        widgets = {
            'dias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Días de abre la discoteca'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horario de atención'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la discoteca'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la discoteca'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género musical'}),
            'servicio1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los servicios'}),
            'servicio2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los servicios'}),
            'servicio3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los servicios'}),
            'sucursales': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'ubicacion_latitud': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Latitud'}),
            'ubicacion_longitud': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Longitud'}),
            'red_social1': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las redes sociales'}),
            'red_social2': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las redes sociales'}),
            'red_social3': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las redes sociales'}),
            'url_video1': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL del video'}),
            'url_video2': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL del video'}),


        }
