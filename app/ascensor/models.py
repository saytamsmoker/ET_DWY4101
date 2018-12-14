from django.db import models

# Create your models here.
# Clase modelo de ascensores
class ModelAsc(models.Model):
    id_mo = models.CharField(primary_key=True, max_length=12, verbose_name="ID Modelo", help_text="ID único para el modelo de ascensor.")
    nom_modasc = models.CharField(max_length=200, verbose_name="Nombre del Modelo", null=False, help_text="Nombre del modelo.")

    def __str__(self):
        return self.nom_modasc

#Clase para identificar cada ascensor
class Ascensor(models.Model):
    id_asc = models.CharField(primary_key=True, max_length=12, verbose_name="ID del ascensor",  help_text="Id unico por ascensor")
    mod_asc = models.ForeignKey(ModelAsc, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id_asc