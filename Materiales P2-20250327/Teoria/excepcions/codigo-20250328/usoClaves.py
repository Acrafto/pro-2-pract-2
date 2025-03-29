# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:06:33 2023

@author: Mariano
"""


def convertirTemp(var):
    try:
        return int(var)
    except ValueError as argumento:
        print('El argumento no contiene un número\n', argumento)


# Llamada a la función.
convertirTemp("xyz")
