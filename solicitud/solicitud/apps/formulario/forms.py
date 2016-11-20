#-*- coding: utf-8 -*-
from django import forms
from .models import *

TIPO_SERVICIO=(
		('Duplicado_Carnet','Duplicado de carnet: valor $5.000'),
		('Duplicado_Constancias','Duplicado de constancias: valor $4.100'),
		('Duplicado_Actas','Duplicado de actas de grado: valor $4.100'),
		('Duplicado_Certificados','Duplicado de certificados: valor $4.100'),
		('Contenidos_Programaticos','Contenidos programáticos: valor $4.100'),
	)

class solicitud_form(forms.Form):

	nombres = forms.CharField(label='Nombres completos',max_length = 50,widget = forms.TextInput())
	apellidos = forms.CharField(label='Apellidos completos',max_length = 50,widget = forms.TextInput())
	cedula = forms.CharField(label='Cedula',max_length = 50,widget = forms.TextInput())
	correo 	= forms.EmailField(label='Correo',max_length = 50,widget = forms.TextInput())
	telefono = forms.CharField(label='Teléfono',max_length = 11,widget = forms.TextInput())
	tipo_servicio = forms.CharField(label='Tipo de Servicio',max_length = 100,widget=forms.Select(choices=TIPO_SERVICIO))
	