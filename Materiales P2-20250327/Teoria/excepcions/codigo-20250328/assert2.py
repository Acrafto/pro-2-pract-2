# -*- coding: utf-8 -*-
"""
Deshabilitar los assert con python -O <fichero.py>
"""


def itemsPares(lista):
    nuevaLista = []
    for i in range(len(lista)-2):
    # for i in range(len(lista)):
        if i % 2 == 0:
            nuevaLista.append(lista[i])
    assert len(nuevaLista) * 2 >= len(lista)
    return nuevaLista


print("__debug__ is {}".format(__debug__))
print(itemsPares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
assert(itemsPares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9])
