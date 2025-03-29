# -*- coding: utf-8 -*-
"""
Ejemplo de uso de una Pila para invertir el orden de los elementos de una Cola

"""

from array_stack import ArrayStack as Stack
from array_queue import ArrayQueue as Queue

q = Queue()
s = Stack()

for c in ['A','B','C']:
    print(f'Enqueueing {c}')
    q.enqueue(c)
   
while not q.is_empty():
    c = q.dequeue()
    print(f'Dequeueing-Pushing {c}')
    s.push(c)
    
while not s.is_empty():
    c = s.pop()
    print(f'Enqueueing {c}')
    q.enqueue(c)    