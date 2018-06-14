from django.db import models

# Create your models here.
class Torneo(models.Model):
	nombre = models.CharField(max_length=70, primary_key=True, default='', unique=True)

	DEPORTE_OPTIONS = (
			('Baloncesto', 'Baloncesto'),
			('Voleibol', 'Voleibol'),
			('Micro-Futbol', 'Micro-Futbol'),
	)

	deporte = models.CharField(max_length=25, choices = DEPORTE_OPTIONS, default = 'Baloncesto', blank=True, null= True)

	fecha = models.DateField()
	SEXO_OPTIONS = (
		('MAS','Masculino'),
		('FEM','Femenino'),
		('MIX','Mixto'),
	)
	sexo = models.CharField(max_length=3, choices=SEXO_OPTIONS, null=True)

	#cantMaxJugadores = models.IntegerField(default = 0)

	def __str__(self):
		return '{} de {} - {}'.format(self.nombre, self.deporte, self.sexo)
