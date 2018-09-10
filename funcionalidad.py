# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(dependientes, estadoCivil, capacidadEndeudamiento, aniosVivienda, aniosTrabajo, edad, edad, email):
	monto = '0'
	if(edad < 18):
		return 'Solicitud denegada. Los prestamos solo se permiten a personas con mayoria de edad.'
	else:
		monto = str(calcularMonto(edad))
	if(aniosTrabajo >= 0 and aniosTrabajo < 2):
		if(capacidadEndeudamiento >= 0.75):
			return 'Acerquese al banco para entregar mas informacion y continuar su tramite.'
		else:
			if(aniosVivienda < 1.5):
				return 'Su solicitud fue DENEGADA.'
			else:
				return 'Su solicitud fue aprobada con un monto de ' + monto + '. Su ejecutiva a cargo es Daniela Arteaga y su cita es el 5 de octubre de 2018. Debe llevar a su cita su cedula y planilla de servicios basicos.'
	else:
		if(estadoCivil == 'soltero'):
			return 'Su solicitud fue DENEGADA.'
		elif(estadoCivil == 'casado'):
			return 'Su solicitud fue aprobada con un monto de ' + monto + '. Su ejecutiva a cargo es Daniela Arteaga y su cita es el 5 de octubre de 2018. Debe llevar a su cita su cedula y planilla de servicios basicos.'
		elif(estadoCivil == 'divorciado'):
			if(dependientes = 0):
				return 'Acerquese al banco para entregar mas informacion y continuar su tramite.'
			elif(dependientes > 0):
				return 'Su solicitud fue aprobada con un monto de ' + monto + '. Su ejecutiva a cargo es Daniela Arteaga y su cita es el 5 de octubre de 2018. Debe llevar a su cita su cedula y planilla de servicios basicos.'

def calcularMonto(edad):
	if(edad < 35 or edad > 65):
		return 80000
	elif(edad >= 35 and edad <=50):
		return 200000
	elif(edad >= 51 and edad <= 65):
		return 120000