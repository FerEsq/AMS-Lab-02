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