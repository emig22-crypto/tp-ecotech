import unittest
from emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_con_factor_por_defecto(self):
        resultado = calcular_emisiones_carbono(100.0)
        self.assertEqual(resultado, 40.0)

    def test_calculo_con_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(100.0, 0.5)
        self.assertEqual(resultado, 50.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0.0)
        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-100.0)


if __name__ == "__main__":
    unittest.main()