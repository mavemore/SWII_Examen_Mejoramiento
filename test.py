# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_ID1(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(2, "married", 75, 1, 0)),"A")
    def test_prueba_ID2(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(2, "single", 75, 1, 0)),"D")
    def test_prueba_ID3(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(2, "divorced", 75, 1, 0)),"Se necesita mas información")
    def test_prueba_ID4(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(2, "divorced", 75, 1, 2)),"A")
    def test_prueba_ID5(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(1, "divorced", 60, 1, 2)),"D")
    def test_prueba_ID6(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(1, "divorced", 60, 3, 2)),"A")
    def test_prueba_ID7(self):
        self.assertEquals((funcionalidad.aprobarPrestamo(1, "divorced", 78, 3, 2)),"A")
            
if __name__ == '__main__':
    unittest.main()