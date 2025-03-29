# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:20:03 2019

@author: mariano
"""

# test_TADClassCard.py
# Programa de prueba del TAD Class Card
from TADClaseCartav2 import Carta

def printAll():
    for palo in 'dpct':
        for valor in range(1, 14):
            carta = Carta (valor, palo)
            print(carta)

if __name__ == '__main__':
    printAll()