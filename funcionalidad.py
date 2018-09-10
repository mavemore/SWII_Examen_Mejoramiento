# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo(anios_trabajo,cap_endeudamiento,estado_civil,anios_vivienda,dependientes):
	"""Funcion que determina si un prestamo es aprobado o no, las validaciones de los valores ingresados (es decir si son aberrantes), se excluyeron,
pues estas validaciones deberían de hacerse en otra funcion"""
	estado=""
	if(anios_trabajo<2): #1
		if(cap_endeudamiento<75): #2
			if(anios_vivienda<1.5): #3
				estado="D" #4
			else:
				estado="A"#5
		else:
			estado="M" #6
	else:
		if(estado_civil=="Married"): #7
			estado="A"#8
		elif(estado_civil=="Single"):#9
			estado="D"#10
		else:
			if(dependientes>0):#11
				estado="A"#12
			else:
				estado="M"#13
	return(estado)#f
