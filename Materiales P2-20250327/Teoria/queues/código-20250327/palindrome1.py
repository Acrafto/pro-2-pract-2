# -*- coding: utf-8 -*-
"""
Ejemplo de uso de una Cola para comprobar si un string es palíndromo

"""

from array_queue import ArrayQueue as Queue

def palindrome(cadena: str):
    q = Queue()
    
    for i in range(len(cadena) // 2): 
        q.enqueue(cadena[i])
    
    i = -1
    while not q.is_empty() and (q.dequeue() == cadena[i]):
        i -= 1
        
    return q.is_empty()

print(palindrome('anilina'))
print(palindrome('arroz'))
print(palindrome('racecar'))