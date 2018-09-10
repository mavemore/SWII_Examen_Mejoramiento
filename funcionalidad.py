# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo(aniosTrabajo, estadoCivil, capacidadEndeuda, aniosVivienda, dependientes):
	
	estado = 'D'
	if aniosTrabajo < 2:
		if capacidadEndeuda < 75:
			if aniosVivienda < 1.5:
				estado = 'D'
			else:
				estado = 'A'
		else:
			estado = 'M'
	else:
		if estadoCivil == 'divorciado':
			if dependientes > 0:
				estado = 'A'
			if dependientes == 0:
				estado = 'M'
		elif estadoCivil == 'soltero':
			estado = 'D'
		elif estadoCivil == 'casado':
			estado = 'A'
		    
	return estado

