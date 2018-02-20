from django.db import models
from apps.torneo.models import Torneo

# Create your models here.
class Equipo(models.Model):
	torneo = models.ForeignKey(Torneo, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(primary_key=True, max_length=35, blank=False, null=False, unique=True)
	puntos = models.IntegerField(default=0, blank=False)
	posicion = models.IntegerField(default=0, blank=False)
	partJug = models.IntegerField(default=0, blank=False)
	partGan = models.IntegerField(default=0, blank=False)
	partPerd = models.IntegerField(default=0, blank=False)
	partW = models.IntegerField(default=0, blank=False)
	cestAfa = models.IntegerField(default=0, blank=False)
	cestCon = models.IntegerField(default=0, blank=False)
	cestDif = models.IntegerField(default=0, blank=False) 

	def __str__(self):
		return '{}'.format(self.nombre)

	def getNombre(self):
		return self.nombre