#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TIPO_SERVICIO=(
		('Duplicado_Carnet','Duplicado de carnet: valor $5.000'),
		('Duplicado_Constancias','Duplicado de constancias: valor $4.100'),
		('Duplicado_Actas','Duplicado de actas de grado: valor $4.100'),
		('Duplicado_Certificados','Duplicado de certificados: valor $4.100'),
		('Contenidos_Programaticos','Contenidos programáticos: valor $4.100'),
	)
# Create your models here.
class Solicitud (models.Model):	

	nombres 		= models.CharField(max_length = 50)
	apellidos 		= models.CharField(max_length = 50)
	cedula 			= models.CharField(max_length = 50)
	correo 			= models.EmailField(max_length = 50)
	telefono 		= models.CharField(max_length = 11)
	tipo_servicio 	= models.CharField(max_length = 100, choices=TIPO_SERVICIO)
	status 			= models.BooleanField(default = False)
	codigo 			= models.CharField(max_length = 100, default=True)
	

	def __unicode__ (self):
		return "Nombre: %s %s ; Tipo de servicio: %s ; Codigo: %s" % (self.nombres,self.apellidos,self.tipo_servicio,self.codigo) 		
