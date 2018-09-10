# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad

# anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_ID1(self):
    	anios_trabajo = 1
    	capacidad_endudamiento = 74
    	anios_vivienda = 1.6
    	estado_civil = ''
    	dependientes = ''
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'A')

    def test_prueba_ID2(self):
    	anios_trabajo = 1
    	capacidad_endudamiento = 74
    	anios_vivienda = 1
    	estado_civil = ''
    	dependientes = ''
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'D')

    def test_prueba_ID3(self):
    	anios_trabajo = 1
    	capacidad_endudamiento = 76
    	anios_vivienda = 1
    	estado_civil = ''
    	dependientes = ''
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'M')

    def test_prueba_ID4(self):
    	anios_trabajo = 2
    	capacidad_endudamiento = ''
    	anios_vivienda = 1
    	estado_civil = 'Divorced'
    	dependientes = 1
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'A')

    def test_prueba_ID5(self):
    	anios_trabajo = 2
    	capacidad_endudamiento = ''
    	anios_vivienda = ''
    	estado_civil = 'Divorced'
    	dependientes = 0
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'M')

    def test_prueba_ID6(self):
    	anios_trabajo = 2
    	capacidad_endudamiento = ''
    	anios_vivienda = ''
    	estado_civil = 'Single'
    	dependientes = 0
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'D')

    def test_prueba_ID7(self):
    	anios_trabajo = 2
    	capacidad_endudamiento = ''
    	anios_vivienda = ''
    	estado_civil = 'Married'
    	dependientes = 0
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'A')

    def test_prueba_ID8(self):
    	anios_trabajo = -1
    	capacidad_endudamiento = ''
    	anios_vivienda = ''
    	estado_civil = 'Married'
    	dependientes = 0
    	aprobado = funcionalidad.aprobar_prestamo(anios_trabajo, capacidad_endudamiento, anios_vivienda, estado_civil, dependientes)
    	self.assertEquals(aprobado, 'No valido')
            
if __name__ == '__main__':
    unittest.main()