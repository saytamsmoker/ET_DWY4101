from django.db import models

# Create your models here.
class Ciudad(models.Model):
    id_ci = models.CharField(primary_key=True, max_length=12)
    nom_ci = models.CharField(max_length=100, verbose_name="Nombre Ciudad", null=False)

    def __str__(self):
        return self.nom_ci

class Comuna(models.Model):
    fk_ci = models.ManyToManyField(Ciudad, verbose_name="Región/Ciudad")
    id_co = models.CharField(primary_key=True, max_length=12)
    nom_co = models.CharField(max_length=100, verbose_name="Nombre Comuna", null=False)

    def __str__(self):
        return self.nom_co

class Cliente(models.Model):
    id_cli = models.CharField(primary_key=True, max_length=12, verbose_name="ID Cliente", help_text="ID único para el Cliente")
    nom_cli = models.CharField(max_length=200, verbose_name="Nombre Cliente", null=False, help_text="Nombre completo del Cliente")
    dir_cli = models.CharField(max_length=150, verbose_name="Dirección del Cliente", null=False, help_text="Dirección de Cliente")
    ci_cli = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    co_cli = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    fon_cli = models.CharField(max_length=13, verbose_name="Número de contacto Cliente", null=False, help_text="Número de telefono de contacto Cliente")
    cor_cli = models.EmailField(max_length=254)

    def __str__(self):
        return self.nom_cli