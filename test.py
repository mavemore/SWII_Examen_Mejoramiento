# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_ID(self):
        self.assertEquals()
    def test_prueba_2(self):
    	resultado = aprobar_prestamo(3,75,"Divorced",3,4)
    	print(resultado)
        self.assertEquals(resultado,"Aprobada")
    def test_prueba_3(self):
    	resultado = aprobar_prestamo(3,75,"Divorced",0,4)
        self.assertEquals(resultado,"Revision Manual")
    def test_prueba_4(self):
    	resultado = aprobar_prestamo(3,75,"Single",3,4)
        self.assertEquals(resultado,"Denegada")
    def test_prueba_5(self):
    	resultado = aprobar_prestamo(3,75,"Married",3,4)
        self.assertEquals(resultado,"Aprobada")
    def test_prueba_6(self):
    	resultado = aprobar_prestamo(1,75,"Married",3,4)
        self.assertEquals(resultado,"Revision Manual")
    def test_prueba_7(self):
    	resultado = aprobar_prestamo(1,70,"Married",3,1)
        self.assertEquals(resultado,"Denegada")
    def test_prueba_8(self):
    	resultado = aprobar_prestamo(1,70,"Married",3,4)
        self.assertEquals(resultado,"Aprobada")



            
if __name__ == '__main__':
    unittest.main()