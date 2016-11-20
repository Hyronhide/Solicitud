from django.conf.urls import patterns, url 
from .views import *

urlpatterns = [		
	
	url(r'^$',Solicitud_View,name = 'vista_solicitud'),
	
	
]	