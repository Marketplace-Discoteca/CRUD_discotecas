from django.db import models # type: ignore

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
    genero = models.CharField(max_length=100, blank=False)  
    servicio1 = models.CharField(max_length=100, blank=True, null=True)
    servicio2 = models.CharField(max_length=100, blank=True, null=True)
    servicio3 = models.CharField(max_length=100, blank=True, null=True)
    sucursales = models.ManyToManyField(Sucursal, blank=True)
    ubicacion_latitud = models.FloatField(blank=True, null=True)
    ubicacion_longitud = models.FloatField(blank=True, null=True)
    red_social1 = models.TextField(blank=True, null=True)
    red_social2 = models.TextField(blank=True, null=True)
    red_social3 = models.TextField(blank=True, null=True)
    url_video1 = models.TextField(blank=True, null=True)
    url_video2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
