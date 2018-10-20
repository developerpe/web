from django import forms
from .models import Suscripcion,Contacto

class SuscripcionForm(forms.ModelForm):
	class Meta:
		model = Suscripcion
		fields = ['correo']
		labels = {
		'correo':'Correo',
		}
		widgets = {
			'correo': forms.EmailInput(
				attrs = {'class' : 'email','placeholder':'Dirección de correo','id':'mc-email'}
			),
		}

class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ['nombre','correo','asunto','mensaje']
		labels = {
			'nombre': 'Nombre',
			'correo':'Correo',
			'asunto': 'Asunto',
			'mensaje': 'Mensaje',
		}
		widgets = {
			'nombre': forms.TextInput(
				attrs = {'class' : 'full-width','placeholder':'Nombre','id':'mc-email'}
			),
			'correo': forms.EmailInput(
				attrs = {'class' : 'full-width','placeholder':'Dirección de correo','id':'mc-email'}
			),
			'asunto': forms.TextInput(
				attrs = {'class' : 'full-width','placeholder':'Asunto','id':'mc-email'}
			),
			'mensaje': forms.TextInput(
				attrs = {'class' : 'full-width','placeholder':'Mensaje','id':'mc-email'}
			),
		}