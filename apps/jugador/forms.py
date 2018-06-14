from django import forms

from .models import Jugador

class JugadorForm(forms.ModelForm):
	class Meta:
		model = Jugador
		fields = ('equipo', 'cedula', 'nombres', 'apellidos', 'sexo', 'edad', 'telefono', 'email', 'domicilio')

	def clean_equipo(self):
		equipo = self.cleaned_data.get('equipo')
		if equipo is None or equipo == '':
			raise forms.ValidationError("El campo 'equipo' no puede ser null, ni vacío.")

		return equipo