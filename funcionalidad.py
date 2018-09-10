# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(anioDeTrabajo, estadoCivil, capEndeudamiento, aniosVivienda, dependientes):
	aprobado = "No"
	if anioDeTrabajo >= 2:
		if estadoCivil == "married":
			aprobado= "A"
		elif estadoCivil == "single":
			aprobado = "D"
		elif estadoCivil == "divorced":
			if dependientes == 0:
				aprobado= "Se necesita mas información"
			elif dependientes > 0:
				aprobado = "A"
	elif anioDeTrabajo < 2:
		if capEndeudamiento < 75:
			if aniosVivienda <1.5:
				aprobado="D"
			elif aniosVivienda >=1.5:
				aprobado ="A"
		elif capEndeudamiento >= 75:
			aprobado="A"
	return aprobado

