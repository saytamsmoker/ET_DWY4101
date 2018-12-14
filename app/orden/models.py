from django.db import models
from app.tecnico.models import User
from app.cliente.models import Cliente
from app.ascensor.models import Ascensor

# Create your models here.
class Orden(models.Model):
    folio = models.IntegerField(primary_key=True)
    fk_cli = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE, verbose_name="Cliente a atender")
    fk_tec = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Tecnico que atiende")
    fecha = models.DateField(verbose_name="Fecha de orden")
    hr_in = models.TimeField(verbose_name="Hora Inicio")
    hr_tr = models.TimeField(null=True, verbose_name="Hora Termino")
    fk_asc = models.ForeignKey(Ascensor, null=True, on_delete=models.CASCADE, verbose_name="Ascensor a trabajar")
    fails = models.TextField(null=True, verbose_name="Fallas detectadas")
    rep = models.TextField(null=True, verbose_name="Reparaciones efectuadas")
    pi_ch = models.TextField(null=True, verbose_name="Piezas cambiadas")
    nom_rec = models.CharField(max_length=50, null=True, verbose_name="Nombre de quien recibe trabajo")

    def __str__(self):
        return str(self.folio)