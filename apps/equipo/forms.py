from django import forms

from .models import Equipo

class EquipoForm(forms.ModelForm):
	class Meta:
		model = Equipo
		fields = ('torneo', 'nombre')

	def clean_torneo(self):
		torneo = self.cleaned_data.get('torneo')
		if torneo is None or torneo == '':
			raise forms.ValidationError("El campo 'torneo' no puede ser null, ni vacío.")

		return torneo

	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')

		if len(nombre)<3:
			raise forms.ValidationError("El nombre debe tener un mínimo de 3 caracteres.")
		return nombre