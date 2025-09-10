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

    def test_count_vowels_happy_path_1(self):
        #Prueba count_vowels con palabra que contiene todas las vocales
        result = count_vowels("programacion")
        self.assertEqual(result, 5)  #o, a, a, i, o

    def test_count_vowels_happy_path_2(self):
        #Prueba count_vowels con mayusculas y acentos
        result = count_vowels("EDUCACIÓN")
        self.assertEqual(result, 5)  #E, U, A, I, Ó

    def test_count_vowels_edge_case_no_vowels(self):
        #Prueba count_vowels con cadena sin vocales
        result = count_vowels("xyz")
        self.assertEqual(result, 0)

    def test_count_vowels_edge_case_empty_string(self):
        #Prueba count_vowels con cadena vacia
        result = count_vowels("")
        self.assertEqual(result, 0)

    def test_count_vowels_error_case_non_string(self):
        #Prueba que count_vowels lance TypeError con entrada no string
        with self.assertRaises(TypeError) as context:
            count_vowels(456)
        self.assertIn("El parametro debe ser una cadena de texto", str(context.exception))

    def test_count_vowels_error_case_list(self):
        #Prueba que count_vowels lance TypeError con lista
        with self.assertRaises(TypeError):
            count_vowels(['a', 'e', 'i'])

    def test_is_palindrome_happy_path_1(self):
        #Prueba is_palindrome con palindromo simple
        result = is_palindrome("anilina")
        self.assertTrue(result)

    def test_is_palindrome_happy_path_2(self):
        #Prueba is_palindrome con palindromo con mayusculas y espacios
        result = is_palindrome("A man a plan a canal Panama")
        self.assertTrue(result)

    def test_is_palindrome_happy_path_3(self):
        #Prueba is_palindrome con palabra que NO es palindromo
        result = is_palindrome("python")
        self.assertFalse(result)

    def test_is_palindrome_edge_case_single_char(self):
        #Prueba is_palindrome con un solo caracter
        result = is_palindrome("a")
        self.assertTrue(result)

    def test_is_palindrome_edge_case_empty_string(self):
        #Prueba is_palindrome con cadena vacia
        result = is_palindrome("")
        self.assertTrue(result)

    def test_is_palindrome_error_case_non_string(self):
        #Prueba que is_palindrome lance TypeError con entrada no string
        with self.assertRaises(TypeError) as context:
            is_palindrome(12321)
        self.assertIn("El parametro debe ser una cadena de texto", str(context.exception))

    def test_is_palindrome_error_case_boolean(self):
        #Prueba que is_palindrome lance TypeError con boolean
        with self.assertRaises(TypeError):
            is_palindrome(True)

    def test_to_upper_happy_path_1(self):
        #Prueba to_upper con palabra en minusculas
        result = to_upper("hola mundo")
        self.assertEqual(result, "HOLA MUNDO")

    def test_to_upper_happy_path_2(self):
        #Prueba to_upper con mezcla de mayusculas, minusculas y acentos
        result = to_upper("Programación en Python")
        self.assertEqual(result, "PROGRAMACIÓN EN PYTHON")

    def test_to_upper_edge_case_already_upper(self):
        #Prueba to_upper con texto ya en mayusculas
        result = to_upper("PYTHON")
        self.assertEqual(result, "PYTHON")

    def test_to_upper_edge_case_empty_string(self):
        #Prueba to_upper con cadena vacia
        result = to_upper("")
        self.assertEqual(result, "")

    def test_to_upper_error_case_non_string(self):
        #Prueba que to_upper lance TypeError con entrada no string
        with self.assertRaises(TypeError) as context:
            to_upper(789)
        self.assertIn("El parametro debe ser una cadena de texto", str(context.exception))

    def test_to_upper_error_case_dict(self):
        #Prueba que to_upper lance TypeError con diccionario
        with self.assertRaises(TypeError):
            to_upper({"text": "hello"})
