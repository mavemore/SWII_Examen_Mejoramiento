# -*- coding: utf-8 -*-
from __future__ import unicode_literals



def aprobar_prestamo(a_trabajo,capacidad_endeudamiento,estado_civil,numero_dependientes,a_vivienda):
	estado_solicitud=""
	if(a_trabajo >= 2):
		if(estado_civil == "Divorced"):
			if(numero_dependientes>0):
				estado_solicitud="Aprobada"
			elif(numero_dependientes==0):
				estado_solicitud = "Revision Manual"
		elif(estado_civil == "Single"):
			estado_solicitud = "Denegada"
		elif(estado_civil == "Married"):
			estado_solicitud = "Aprobada"
	elif(a_trabajo <2):
		if(capacidad_endeudamiento>=75):
			estado_solicitud = "Revision Manual"
		elif(capacidad_endeudamiento <75):
			if(a_vivienda < 1.5):
				estado_solicitud = "Denegada"
			elif(a_vivienda >= 1.5):
				estado_solicitud = "Aprobada"

	return estado_solicitud




