# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo):
	if (a_trabajo < 2):
		if (capacidad_endeudamiento < 75):
			if (a_vivienda < 1.5):
				return 'Denegado'
			else:
				return 'Aprobado'
		else:
			return 'Manual'
	else:
		if (estado_civil == 'D'):
			if (numero_dependientes > 0):
				return 'Aprobado'
			if (numero_dependientes == 0):
				return 'Manual'
		elif (estado_civil == 'S'):
				return 'Denegado'
		elif (estado_civil == 'C'):
				return 'Aprobado'