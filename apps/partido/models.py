from django.db import models
from apps.equipo.models import Equipo

# Create your models here.
class Partido(models.Model):
	equipoLoc = models.CharField(max_length=30, default='Equipo Local')
	equipoVis = models.CharField(max_length=30, default='Equipo Visitante')
	fecha = models.DateField()
	ronda = models.IntegerField()
	cestasLocal = models.IntegerField()
	cestasVisit = models.IntegerField()
	faltasLocal = models.IntegerField()
	faltasVisit = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.equipoLoc+" vs "+self.equipoVis)