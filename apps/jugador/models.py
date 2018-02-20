from django.db import models
from apps.equipo.models import Equipo

# Create your models here.
class Jugador(models.Model):
	cedula = models.CharField(max_length=12, primary_key=True)
	equipo = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.CASCADE)
	nombres = models.CharField(max_length=25, default='', blank=False)
	apellidos = models.CharField(max_length=25, default='', blank=False)
	SEXO_OPTIONS = (
		('MAS','Masculino'),
		('FEM','Femenino'),
	)
	sexo = models.CharField(max_length=3, choices=SEXO_OPTIONS, blank=False)
	edad = models.IntegerField(blank=False)
	telefono = models.CharField(max_length=12, blank=True)
	email = models.EmailField(max_length=40, blank=True)
	domicilio = models.TextField(max_length=30, blank=True)

	def esMayor(self):   # semi-master es un torneo para señores mayores de edad
		if self.edad >= 40:
			return True
		else:
			return False

	esMayor.short_description = 'Apto Semi-master'

	def __str__(self):
		return '{} {} - {}'.format(self.nombres, self.apellidos, self.equipo.nombre)