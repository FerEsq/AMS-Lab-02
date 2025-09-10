'''
 * Nombre: test_textManipulation.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Descripción: Pruebas unitarias para todas las funciones de manipulación de texto
 * Lenguaje: Python
 * Historial: 
    - Creado el 09.09.2025
    - Modificado el 09.09.2025
'''

import unittest
from textManipulation import reverse, count_vowels, is_palindrome, to_upper, concat

'''
Clase de pruebas unitarias para la libreria textManipulation
'''
class TestTextManipulation(unittest.TestCase):
    def test_reverse_happy_path_1(self):
        #Prueba reverse con una palabra simple
        result = reverse("hola")
        self.assertEqual(result, "aloh")

    def test_reverse_happy_path_2(self):
        #Prueba reverse con una frase con espacios
        result = reverse("python es genial")
        self.assertEqual(result, "laineg se nohtyp")

    def test_reverse_edge_case_empty_string(self):
        #Prueba reverse con cadena vacia
        result = reverse("")
        self.assertEqual(result, "")

    def test_reverse_error_case_non_string(self):
        #Prueba que reverse lance TypeError con entrada no string
        with self.assertRaises(TypeError) as context:
            reverse(123)
        self.assertIn("El parametro debe ser una cadena de texto", str(context.exception))

    def test_reverse_error_case_none(self):
        #Prueba que reverse lance TypeError con None
        with self.assertRaises(TypeError):
            reverse(None)
            