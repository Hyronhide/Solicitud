#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def Solicitud_View (request):
	info_enviado = False 
	correo = ""
	nombres  = ""
	apellidos = ""
	cedula = ""
	telefono = ""
	tipo_servicio = ""
	servicio = " "
	servicio_usuario = ""
	
	if request.method == "POST":
		formulario = solicitud_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			correo 	= formulario.cleaned_data['correo']
			nombres = formulario.cleaned_data['nombres']
			apellidos = formulario.cleaned_data['apellidos']
			cedula = formulario.cleaned_data['cedula']
			telefono = formulario.cleaned_data['telefono']
			tipo_servicio = formulario.cleaned_data['tipo_servicio']
			
			
			if tipo_servicio == 'Duplicado_Carnet':
				servicio = "Duplicado de carnet"
				servicio_usuario = "Duplicado de carnet: valor $5.000, Entregar a Marta Lucia Muñoz"

			if tipo_servicio == 'Duplicado_Constancias':
				servicio = "Duplicado de constancias"
				servicio_usuario = "Duplicado de constancias: valor $4.100, Entregar a Marta Lucia Muñoz"

			if tipo_servicio == 'Duplicado_Actas':
				servicio = "Duplicado de actas de grado" 
				servicio_usuario = "Duplicado de actas de grado: valor $4.100, Entregar a Marta Lucia Muñoz"

			if tipo_servicio == 'Duplicado_Certificados':
				servicio = "Duplicado de certificados" 
				servicio_usuario = "Duplicado de certificados: valor $4.100, Entregar a Libardo Arias"

			if tipo_servicio == 'Contenidos_Programaticos':
				servicio = "Contenidos programaticos" 	
				servicio_usuario = "Contenidos programaticos: valor $4.100, Entregar a Luz Marina Ríos"		 	 

			'''Bloque configuracion de envio por GMAIL'''
			to_admin = 'lgonzalez21@misena.edu.co'
			#o_admin = 'drmosquera90@misena.edu.co'
			to_user = correo
			html_content_admin = "<p><b>Solicitud de servicio: </b>%s</p><br> <b>Nombres</b>: %s <br><br> <b>Apellidos</b>: %s  <br><br> <b>Correo:</b> %s  <br><br> <b>Cedula:</b> %s  <br><br> <b>Telefono:</b> %s "%(servicio,nombres,apellidos,correo,cedula,telefono)
			html_content_user = "<p><b>Solicitud de servicio: </b>%s</p><br> -Debe imprimir únicamente copia de banco.<br>-Debe hacer consignación en Bancolombia, no corresponsales bancarios.<br>-Una vez consigne o cancele su recibo debe hacerlos llegar a las oficinas de coordinación académica según su solicitud ,en este caso:  %s.<br>-La consignación debe hacerse el mismo día que se genera el recibo.<br>-Debe imprimir el recibo en impresora laser.<br>"%(servicio,servicio_usuario)

			msg = EmailMultiAlternatives('Solicitud de recibo de consignacion', html_content_admin, 'from@gmail.com',[to_admin])
			msg2 = EmailMultiAlternatives('Solicitud de recibo de consignacion (Recuerde esto al momento de obtener el recibo)', html_content_user, 'from@gmail.com',[to_user])
			msg.attach_alternative(html_content_admin,'text/html')
			
			msg2.attach_alternative(html_content_user,'text/html')
			msg2.send()
			msg.send()
			'''Fin del bloque'''
	else:
		formulario = solicitud_form()		
	ctx = {'form':formulario, 'correo':correo, 'nombres':nombres, 'apellidos':apellidos, 'cedula':cedula, 'telefono':telefono, 'tipo_servicio': tipo_servicio, 'info_enviado': info_enviado}	
	return render(request,'formulario/solicitud.html',ctx)
