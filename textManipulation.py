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