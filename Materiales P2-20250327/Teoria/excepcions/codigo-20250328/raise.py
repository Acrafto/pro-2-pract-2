# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:08:00 2020

@author: Mariano
"""
def minimo (arg1, arg2):
    if arg1 is None or arg2 is None:
        raise TypeError("Argumentos para minimo() no pueden ser None")
    if arg1 < arg2:
        return arg1
    else:
        return arg2
    
print(minimo(1,None))