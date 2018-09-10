# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad
from funcionalidad import *


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
    	resultado = aprobarPrestamo(0,'soltero', 0.5, 5, 3, 15, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD DENEGADA')

    def test_prueba_2(self):
    	resultado = aprobarPrestamo(0,'soltero', 0.8, 5, 1, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD MANUAL')

    def test_prueba_3(self):
    	resultado = aprobarPrestamo(0,'soltero', 0.5, 1, 1, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD DENEGADA')

    def test_prueba_4(self):
    	resultado = aprobarPrestamo(0,'soltero', 0.5, 2, 1, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD APROBADA')

    def test_prueba_5(self):
    	resultado = aprobarPrestamo(0,'soltero', 0.5, 2, 5, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD DENEGADA')

    def test_prueba_6(self):
    	resultado = aprobarPrestamo(0,'casado', 0.5, 2, 5, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD APROBADA')

    def test_prueba_7(self):
    	resultado = 7probarPrestamo(0,'divorciado', 0.5, 2, 5, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD MANUAL')

    def test_prueba_8(self):
    	resultado = aprobarPrestamo(5,'divorciado', 0.5, 2, 5, 20, 'ejemplo@mail.com')
        self.assertEquals(resultado, 'SOLICITUD APROBADA')
            
if __name__ == '__main__':
    unittest.main()


