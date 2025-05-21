
'''
Realizar test de los ejercicios de la semana_02 y subirlos al repo bajo el 
nombre test_semana_02.py.
Debe haber al menos 3 test por ejercicio.-
'''

import unittest

def invertir_lista(lista):
    return lista[::-1]

def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  
        else:
            n = n * 3 + 1
        pasos += 1
    return pasos

def contar_definiciones(diccionario):
    return {clave: len(definiciones) for clave, definiciones in diccionario.items()}

def cantidad_de_claves_letra(diccionario, letra):
    return sum(1 for clave in diccionario if clave.startswith(letra))


class TestEjercicio1_InvertirLista(unittest.TestCase):
    def test_lista_numerica(self):
        self.assertEqual(invertir_lista([1, 2, 3]), [3, 2, 1])

    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

    def test_lista_strings(self):
        self.assertEqual(invertir_lista(["uno", "dos", "tres"]), ["tres", "dos", "uno"])

    def test_lista_mixta(self):
        self.assertEqual(invertir_lista([1, "dos", 3.0]), [3.0, "dos", 1])

class TestEjercicio2_Collatz(unittest.TestCase):
    def test_collatz_1(self):
        self.assertEqual(collatz(1), 0)

    def test_collatz_6(self):
        self.assertEqual(collatz(6), 8)

    def test_collatz_3(self):
        self.assertEqual(collatz(3), 7)

    def test_collatz_numero_grande(self):
        self.assertEqual(collatz(27), 111)

class TestEjercicio3_Diccionarios(unittest.TestCase):
    def test_contar_definiciones(self):
        dicc = {
            "agua": ["líquido", "incolora"],
            "fuego": ["calor", "luz", "combustión"]
        }
        esperado = {
            "agua": 2,
            "fuego": 3
        }
        self.assertEqual(contar_definiciones(dicc), esperado)

    def test_contar_definiciones_vacio(self):
        self.assertEqual(contar_definiciones({}), {})

    def test_cantidad_claves_con_letra(self):
        dicc = {
            "gas": [],
            "gato": [],
            "perro": [],
            "guitarra": [],
        }
        self.assertEqual(cantidad_de_claves_letra(dicc, "g"), 3)

    def test_cantidad_claves_con_letra_sin_resultado(self):
        dicc = {
            "uno": [],
            "dos": [],
            "tres": [],
        }
        self.assertEqual(cantidad_de_claves_letra(dicc, "z"), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)