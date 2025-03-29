# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:49:40 2019

@author: mariano
"""

# Módulo implementando el TAD Card con funciones

_PALOS = 'cdpt'
_NOMBRES_PALOS = ['corazones','diamantes','picas','tréboles']

_VALORES = range(1,14)
_NOMBRES_VALORES = [ ' As ' , ' Dos ' , ' Tres ' , ' Cuatro ' , ' Cinco ' , \
                  ' Seis ' ,' Siete ' , ' Ocho ' , ' Nueve ' , ' Diez ' , \
                  ' Jota ' , ' Reina ' , ' Rey ' ]

def create(valor, palo):
    assert valor in _VALORES and palo in _PALOS
    return (valor, palo )

def valor (card):
    return card[0]

def palo (card):
    return card[1]

def nombrePalo (card) :
    index = _PALOS.index ( palo (card) )
    return _NOMBRES_PALOS [index]

def nombreValor (card) :
    index = _VALORES.index ( valor (card) )
    return _NOMBRES_VALORES [index]

def toString (card) :
    return nombreValor (card) + ' de ' + nombrePalo (card)