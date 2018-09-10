# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo (anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes):
	if (0 <= anios_trabajo < 2) :
		if (0 <= capacidad_endudamiento < 75):
			if (anios_vivienda < 1.5):
				return 'D'
			else:
				return 'A'
		elif (capacidad_endudamiento > 75):
			return 'M'
	elif (anios_trabajo >= 2):
		if (estado_civil == 'Divorced'):
			if (dependientes > 0):
				return 'A'
			elif (dependientes == 0):
				return 'M'
		elif (estado_civil == 'Single'):
			return 'D'
		elif (estado_civil == 'Married'):
			return 'A'
	return 'No valido'
