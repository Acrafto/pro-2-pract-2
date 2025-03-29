# -*- coding: utf-8 -*-
"""
Ejemplo de uso de una Pila para comprobar si un string es palíndromo
"""

from array_stack import ArrayStack as Stack

def palindrome(cadena: str):
    s = Stack()
    
    for item in cadena:
        s.push(item)
    
    i = 0
    while not s.is_empty() and (s.pop() == cadena[i]):
        i += 1
        
    return s.is_empty()

print(palindrome('anilina'))
print(palindrome('arroz'))
print(palindrome('racecar'))
