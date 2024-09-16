from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    direccion = models.CharField(max_length=255, blank=False)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Discoteca(models.Model):
    dias = models.CharField(max_length=100, default="No especificado", blank=False)
    horario = models.CharField(max_length=100, default="No especificado", blank=False)
    nombre = models.CharField(max_length=100, blank=False)
    direccion = models.CharField(max_length=255, blank=False)
    descripcion = models.TextField(blank=True, null=True)
    genero = models.CharField(max_length=100, blank=False)  # Género de música
    servicio1 = models.CharField(max_length=100, blank=True, null=True)  # Lista de servicios
    servicio2 = models.CharField(max_length=100, blank=True, null=True)  # Lista de servicios
    servicio3 = models.CharField(max_length=100, blank=True, null=True)  # Lista de servicios
    sucursales = models.ManyToManyField(Sucursal, blank=True)  # Relación con Sucursales
    ubicacion_latitud = models.FloatField(blank=True, null=True)
    ubicacion_longitud = models.FloatField(blank=True, null=True)
    red_social1 = models.TextField(blank=True, null=True)  # Lista de redes sociales
    red_social2 = models.TextField(blank=True, null=True)  # Lista de redes sociales
    red_social3 = models.TextField(blank=True, null=True)  # Lista de redes sociales
    url_video1 = models.TextField(blank=True, null=True)  # Video 1
    url_video2 = models.TextField(blank=True, null=True)  # Video 2
    

    def __str__(self):
        return self.nombre
