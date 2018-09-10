# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo(anos_trabaj0, endeudamiento, vivienda, estado_civil, dependientes):
	"""Analiza si el cliente cumple o no la precalificacion del prestamo"""
	precailificado == ""
	if anos_trabaj0 < 2:
		if endeudamiento < 0.75:
			if vivienda >= 1.5:
				precailificado == 'aprobado'
				else
				precailificado == 'denegado'
			else
			precailificado == 'manual'
		elif estado_civil == 'casado':
			precailificado == 'aprobado'
		elif estado_civil == 'soltero':
			precailificado == 'denegado'
		elif dependientes<0:
			precailificado == 'aprobado'
			else
			precailificado == 'manual'
		return precailificado

