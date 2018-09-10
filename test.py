# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad as fun


class Test(unittest.TestCase):
	
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
	#aprobar_prestamo(aniosTrabajo, estadoCivil, capacidadEndeuda, aniosVivienda, dependientes)
	def test_prueba_C01(self):
		result = fun.aprobar_prestamo(1,'casado',65,1,1)
		self.assertEquals(result,'D')
		
	def test_prueba_C02(self):
		result = fun.aprobar_prestamo(1,'casado',65,2,1)
		self.assertEquals(result,'A')
		
	def test_prueba_C03(self):
		result = fun.aprobar_prestamo(1,'casado',75,1,1)
		self.assertEquals(result,'M')
		
	def test_prueba_C04(self):
		result = fun.aprobar_prestamo(2,'divorciado',75,1,1)
		self.assertEquals(result,'A')
		
	def test_prueba_C05(self):
		result = fun.aprobar_prestamo(2,'divorciado',75,1,0)
		self.assertEquals(result,'M')
		
	def test_prueba_C06(self):
		result = fun.aprobar_prestamo(2,'soltero',75,1,0)
		self.assertEquals(result,'D')
		
	def test_prueba_C07(self):
		result = fun.aprobar_prestamo(2,'casado',75,1,0)
		self.assertEquals(result,'A')
		
if __name__ == '__main__':
	unittest.main()
	
	
	
