# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad as funcionalidad


class Test(unittest.TestCase):

	def test_CC_1(self):
		numero_dependientes = 0
		estado_civil = 'S'
		capacidad_endeudamiento = 70
		a_vivienda = 1
		a_trabajo = 1

		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Denegado')

	def test_CC_2(self):
		numero_dependientes = 0
		estado_civil = 'S'
		capacidad_endeudamiento = 70
		a_vivienda = 3
		a_trabajo = 1
		
		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Aprobado')

	def test_CC_3(self):
		numero_dependientes = 0
		estado_civil = 'S'
		capacidad_endeudamiento = 80
		a_vivienda = 1
		a_trabajo = 1
		
		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Manual')

	def test_CC_4(self):
		a_trabajo = 3
		capacidad_endeudamiento = 70
		a_vivienda = 1
		estado_civil = 'D'
		numero_dependientes = 2

		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Aprobado')

	def test_CC_5(self):
		a_trabajo = 3
		capacidad_endeudamiento = 70
		a_vivienda = 1
		estado_civil = 'D'
		numero_dependientes = 0

		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Manual')

	def test_CC_6(self):
		a_trabajo = 3
		capacidad_endeudamiento = 70
		a_vivienda = 1
		estado_civil = 'S'
		numero_dependientes = 2

		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Denegado')

	def test_CC_7(self):
		a_trabajo = 3
		capacidad_endeudamiento = 70
		a_vivienda = 1
		estado_civil = 'C'
		numero_dependientes = 2

		resultado = funcionalidad.aprobarPrestamo (numero_dependientes, estado_civil, capacidad_endeudamiento, a_vivienda, a_trabajo)
		self.assertEqual(resultado, 'Aprobado')
						
if __name__ == '__main__':
		unittest.main()