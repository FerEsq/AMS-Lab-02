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

    def test_concat_happy_path_1(self):
        #Prueba concat con dos palabras simples
        result = concat("Hola", " mundo")
        self.assertEqual(result, "Hola mundo")

    def test_concat_happy_path_2(self):
        #Prueba concat con cadenas que contienen numeros y simbolos
        result = concat("Python", "3.11")
        self.assertEqual(result, "Python3.11")

    def test_concat_edge_case_empty_strings(self):
        #Prueba concat con cadenas vacias
        result = concat("", "")
        self.assertEqual(result, "")

    def test_concat_edge_case_one_empty(self):
        #Prueba concat con una cadena vacia
        result = concat("Hello", "")
        self.assertEqual(result, "Hello")

    def test_concat_error_case_first_not_string(self):
        #Prueba que concat lance TypeError cuando el primer parametro no es string
        with self.assertRaises(TypeError) as context:
            concat(123, "world")
        self.assertIn("Ambos parametros deben ser cadenas de texto", str(context.exception))

    def test_concat_error_case_second_not_string(self):
        #Prueba que concat lance TypeError cuando el segundo parametro no es string
        with self.assertRaises(TypeError) as context:
            concat("Hello", 456)
        self.assertIn("Ambos parametros deben ser cadenas de texto", str(context.exception))

    def test_concat_error_case_both_not_string(self):
        #Prueba que concat lance TypeError cuando ambos parametros no son string
        with self.assertRaises(TypeError):
            concat(123, 456)

    def test_concat_error_case_none_values(self):
        #Prueba que concat lance TypeError con valores None
        with self.assertRaises(TypeError):
            concat(None, None)


'''
Pruebas adicionales para confirmar que los tests fallan cuando las funciones no cumplen con lo esperado
'''
class TestFunctionFailures(unittest.TestCase):
    #Esta prueba demuestra que si reverse() retornara la cadena sin invertir, el test fallaria
    def test_reverse_would_fail_with_wrong_implementation(self):
        #Si reverse() estuviera mal implementada y retornara s en lugar de s[::-1]
        result = reverse("test")
        #Esta assertion pasaría si reverse() fuera incorrecta
        self.assertNotEqual(result, "test")  #Confirma que SI esta invertida
    
    #Esta prueba demuestra que si count_vowels() contara mal, el test fallaria
    def test_count_vowels_would_fail_with_wrong_count(self):
        result = count_vowels("hello")  #Deberia ser 2 (e, o)
        #Si la funcion contara consonantes en lugar de vocales, esto fallaria
        self.assertEqual(result, 2)
        self.assertNotEqual(result, 3)  #No debería ser 3

    #Esta prueba demuestra que si is_palindrome() no manejara correctamente los casos, fallaria
    def test_is_palindrome_would_fail_with_wrong_logic(self):
        #Si no limpiara espacios y mayusculas, esto fallaria
        result = is_palindrome("A man a plan a canal Panama")
        self.assertTrue(result)
        
        #Si retornara siempre True, esto fallaria
        result_false = is_palindrome("not a palindrome")
        self.assertFalse(result_false)
