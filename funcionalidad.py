# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(dependientes, estadoCivil, capacidadEndeudamiento, aniosVivienda, aniosTrabajo, edad, email):
	if(edad < 18):
		return 'SOLICITUD DENEGADA'
	if(aniosTrabajo < 2):
		if(capacidadEndeudamiento >= 0.75):
			return 'SOLICITUD MANUAL'
		else:
			if(aniosVivienda < 1.5):
				return 'SOLICITUD DENEGADA.'
			else:
				return 'SOLICITUD APROBADA'
	else:
		if(estadoCivil == 'soltero'):
			return 'SOLICITUD DENEGADA'
		elif(estadoCivil == 'casado'):
			return 'SOLICITUD APROBADA'
		elif(estadoCivil == 'divorciado'):
			if(dependientes == 0):
				return 'SOLICITUD MANUAL'
			elif(dependientes > 0):
				return 'SOLICITUD APROBADA'

