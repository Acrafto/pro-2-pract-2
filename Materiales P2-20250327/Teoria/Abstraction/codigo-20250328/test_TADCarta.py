# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:15:21 2019

@author: mariano
"""
# test_TADCard.py
# Programa de prueba del TAD Card
import TADCarta

def printAll():
    for p in 'cdpt':
        for v in range(1, 14):
            carta = TADCarta.create(v,p)
            print (TADCarta.toString(carta))
      
if __name__ == '__main__':
    printAll()