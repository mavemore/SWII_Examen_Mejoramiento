# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from funcionalidad import aprobar_prestamo


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
#anios_trabajo,cap_endeudamiento,estado_civil,anios_vivienda,dependientes
    def test_prueba_1(self):
        anios_trabajo = 1
        cap_endeudamiento = 74
        estado_civil = "Divorced"
        anios_vivienda = 1.4
        dependientes = 0
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"D")

    def test_prueba_2(self):
        anios_trabajo = 1
        cap_endeudamiento = 74
        estado_civil = "Married"
        anios_vivienda = 1.5
        dependientes = 2
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"A")

    def test_prueba_3(self):
        anios_trabajo = 1
        cap_endeudamiento = 75
        estado_civil = "Divorced"
        anios_vivienda = 1.4
        dependientes = 1
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"M")

    def test_prueba_4(self):
        anios_trabajo = 2
        cap_endeudamiento = 74
        estado_civil = "Married"
        anios_vivienda = 1.4
        dependientes = 0
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"A")

    def test_prueba_5(self):
        anios_trabajo = 2
        cap_endeudamiento = 74
        estado_civil = "Single"
        anios_vivienda = 1.4
        dependientes = 0
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"D")

    def test_prueba_6(self):
        anios_trabajo = 2
        cap_endeudamiento = 74
        estado_civil = "Divorced"
        anios_vivienda = 1.4
        dependientes = 1
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"A")

    def test_prueba_7(self):
        anios_trabajo = 2
        cap_endeudamiento = 74
        estado_civil = "Divorced"
        anios_vivienda = 1.4
        dependientes = 0
        estado_prestamo = aprobar_prestamo(anios_trabajo,cap_endeudamiento, estado_civil, anios_vivienda, dependientes)
        self.assertEquals(estado_prestamo,"M")
            
if __name__ == '__main__':
    unittest.main()

