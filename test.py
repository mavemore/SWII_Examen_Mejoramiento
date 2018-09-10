# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from funcionalidad import *
import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
        estado = AprobarPrestamo(1,75,"casado",0,1.5)
        self.assertEquals(estado, "Revision Manual")

    def test_prueba_2(self):
        estado = AprobarPrestamo(1,70,"casado",0,1.5)
        self.assertEquals(estado, "Aprobado")

    def test_prueba_3(self):
        estado = AprobarPrestamo(1,70,"casado",0,1.4)
        self.assertEquals(estado, "Denegado")

    def test_prueba_4(self):
        estado = AprobarPrestamo(2,70,"casado",0,1.4)
        self.assertEquals(estado, "Aprobado")

    def test_prueba_5(self):
        estado = AprobarPrestamo(2,70,"Soltero",0,1.4)
        self.assertEquals(estado, "Denegado")

    def test_prueba_6(self):
        estado = AprobarPrestamo(2,70,"viudo",0,1.4)
        self.assertEquals(estado, "Estado Civil incorrecto.")

    def test_prueba_7(self):
        estado = AprobarPrestamo(2,70,"divorciado",0,1.4)
        self.assertEquals(estado, "Revision Manual")

    def test_prueba_8(self):
        estado = AprobarPrestamo(2,70,"divorciado",2,1.4)
        self.assertEquals(estado, "Aprobado")

    def test_prueba_9(self):
        estado = AprobarPrestamo(2,70,"divorciado",-2,1.4)
        self.assertEquals(estado, "Numero de dependientes incorrectos.")
 
if __name__ == '__main__':
    unittest.main()