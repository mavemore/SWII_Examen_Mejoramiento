# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(anios_trabajo, capacidad_endeudamiento, estado_civil, dependientes, anios_vivencia_actual):
    if anios_trabajo < 2:
        if capacidad_endeudamiento < 75:
            if anios_vivencia_actual < 1.5:
                return "Denegado"
            else:
                return "Aprobado"
        else:
            return "Revision Manual"
    elif anios_trabajo >= 2:
        if estado_civil.lower() == "casado":
            return "Aprobado"
        elif estado_civil.lower() == "soltero":
            return "Denegado"
        elif estado_civil.lower() == "divorciado":
            if dependientes == 0:
                return "Revision Manual"
            elif dependientes > 0:
                return "Aprobado"
            else:
                return "Numero de dependientes incorrectos."
        else:
            return "Estado Civil incorrecto."