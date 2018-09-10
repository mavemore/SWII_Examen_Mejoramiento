# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    #anos_trabaj0, endeudamiento, vivienda, estado_civil, dependientes
    #caso 01: años de trabajo no admitido
    def test_prueba_01(self):
        self.assertEquals(aprobar_prestamo(-1,0.5,2,'casado',2),'Usted no precalifica: Los años de trabajo no es un valor permitido')

    #caso 02: Precalificación con 1 año de trabajo, 0.58 de endedudamiento, y 2 años en la vivienda actual
    def test_prueba_02(self):
        self.assertEquals(aprobar_prestamo(1,0.58,2,'casado',2),'aprobado')

    #caso 03: Precalificación con 1 año de trabajo, 0.58 de endedudamiento, y 1 año en la vivienda actual
    def test_prueba_03(self):
        self.assertEquals(aprobar_prestamo(1,0.58,1,'casado',2),'denegado')
 	
 	#caso 04: Precalificación con 1 año de trabajo y 0.80 de endedudamiento
    def test_prueba_04(self):
        self.assertEquals(aprobar_prestamo(1,0.8,2,'casado',2),'manual')

    #caso 05: Precalificación con 3 años de trabajo, y estado civil casado
    def test_prueba_05(self):
        self.assertEquals(aprobar_prestamo(3,0.58,2,'casado',2),'aprobado')

   	#caso 06: Precalificación con 3 años de trabajo, y estado civil soltero
    def test_prueba_06(self):
        self.assertEquals(aprobar_prestamo(3,0.58,2,'soltero',2),'denegado')

    #caso 07: Precalificación con 3 año de trabajo estado civil divorciado y dependientes 2
    def test_prueba_07(self):
        self.assertEquals(aprobar_prestamo(3,0.58,2,'divorciado',2),'aprobado')

    #caso 08: Precalificación con 3 año de trabajo, estado civil divorciado y 0 dependientes
    def test_prueba_08(self):
        self.assertEquals(aprobar_prestamo(3,0.58,2,'divorciado',0),'manual')
if __name__ == '__main__':
    unittest.main()
