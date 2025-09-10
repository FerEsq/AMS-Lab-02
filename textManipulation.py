'''
 * Nombre: textManipulation.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Descripción: Librería para realizar operaciones comunes de manipulación de cadenas de texto
 * Lenguaje: Python
 * Historial: 
    - Creado el 09.09.2025
    - Modificado el 09.09.2025
'''

'''
Retorna una cadena de texto en orden inverso

Args:
    s (str): La cadena de texto a invertir
    
Returns:
    str: La cadena invertida
'''
def reverse(s):
    if not isinstance(s, str):
        raise TypeError("El parametro debe ser una cadena de texto")
    
    return s[::-1]

'''
Retorna el total de vocales que tiene una cadena de texto

Args:
    s (str): La cadena de texto a analizar
    
Returns:
    int: El numero total de vocales (a, e, i, o, u)
'''
def count_vowels(s):
    if not isinstance(s, str):
        raise TypeError("El parametro debe ser una cadena de texto")
    
    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
            
    return count

'''
Retorna si una cadena de texto es palindromo o no

Args:
    s (str): La cadena de texto a verificar
    
Returns:
    bool: True si es palindromo, False en caso contrario
'''
def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("El parametro debe ser una cadena de texto")
    
    #Convertir a minusculas y eliminar espacios para una comparacion mas robusta
    clean_s = s.lower().replace(" ", "")
    
    #Comparar la cadena con su reverso
    return clean_s == clean_s[::-1]

'''
Retorna una cadena de texto en mayusculas

Args:
    s (str): La cadena de texto a convertir
    
Returns:
    str: La cadena en mayusculas
'''
def to_upper(s):
    if not isinstance(s, str):
        raise TypeError("El parametro debe ser una cadena de texto")
    
    return s.upper()

'''
Retorna una cadena de texto que une dos cadenas de texto

Args:
    a (str): Primera cadena de texto
    b (str): Segunda cadena de texto
    
Returns:
    str: La concatenacion de ambas cadenas
'''
def concat(a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Ambos parametros deben ser cadenas de texto")
    
    return a + b