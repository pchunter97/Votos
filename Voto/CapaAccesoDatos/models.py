from django.db import models

from simple_history.models import HistoricalRecords

# Create your models here.
#Crea el modelo padron con elector_ci, nombre_elector, apellido_elector, correo_institucional, nivel_elector, hash, registro_voto
class t_padron_electoral(models.Model):
    elector_ci = models.IntegerField(primary_key=True)
    nombre_elector = models.CharField(max_length=50)
    apellido_elector = models.CharField(max_length=50)
    correo_institucional = models.EmailField(max_length=50)
    nivel_elector = models.CharField(max_length=50)
    hash = models.CharField(max_length=50)
    registro_voto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_elector + " " + self.apellido_elector

#Crea el modelo t_datos_eleccion id_datos_eleccion, nombre_eleccion, fecha_eleccion, hora_inicio, hora_fin
class t_datos_eleccion(models.Model):
    id_datos_eleccion = models.AutoField(primary_key=True)
    nombre_eleccion = models.CharField(max_length=50)
    fecha_eleccion = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return self.nombre_eleccion

#Crea el modelo t_partido con id_partido, partido_img, partido_nombre, partido_candidato_img, nombre_candidato_principal
class t_partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    partido_img = models.ImageField(upload_to='partidos/')
    partido_nombre = models.CharField(max_length=50)
    partido_candidato_img = models.ImageField(upload_to='partidos/')
    nombre_candidato_principal = models.CharField(max_length=50)

    def __str__(self):
        return self.partido_nombre
#Crea el modelo t_voto con id_voto,  id_partido, tipo_voto, voto_fecha relacionando id_partido con id_partido de t_partido
class t_voto(models.Model):
    id_voto = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey(t_partido, on_delete=models.CASCADE)
    tipo_voto = models.CharField(max_length=50)
    voto_fecha = models.DateField()
    history = HistoricalRecords()

    def __str__(self):
        return self.tipo_voto

#Crea el modelo t_escrutinio con id_escrutinio, votos_totales, votos_validos, votos_invalidos, votos_nulos, votos_blancos,id_voto relacionando uno a muchos con id_voto de t_voto
class t_escrutinio(models.Model):
    id_escrutinio = models.AutoField(primary_key=True)
    votos_totales = models.IntegerField()
    votos_validos = models.IntegerField()
    votos_invalidos = models.IntegerField()
    votos_nulos = models.IntegerField()
    votos_blancos = models.IntegerField()
    id_voto = models.ForeignKey(t_voto, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_escrutinio

#Crea tabla de registro de cambios de la tabla t_voto

class Auditoria_Voto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, blank=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=255, blank=True, editable=False)

    


