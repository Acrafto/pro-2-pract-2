# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:57:00 2019

@author: mariano
"""
# TADClassCardv2.py
    
class Carta:
    """Un simple juego de cartas. Una carta se representa por un número
    entre 0 y 51 correspondiente a su orden en la baraja: primero las
    13 cartas de corazones, luego las 13 de diamantes, las 13 de picas y
    por último las 13 de tréboles"""

    VALORES = range(1,14)
    NOMBRES_VALORES = [ ' As ' , ' Dos ' , ' Tres ' , ' Cuatro ' , ' Cinco ' , \
                        ' Seis ' ,' Siete ' , ' Ocho ' , ' Nueve ' , ' Diez ' , \
                        ' Jota ' , ' Reina ' , ' Rey ' ]    

    PALOS = 'cdpt'
    NOMBRES_PALOS = ['corazones','diamantes','picas','tréboles']

    
    def __init__(self, valor, palo):
        """Crea una carta del valor y palo dados
		in: Un valor y un palo
        out: Una nueva carta
        pre: valor en el rango(1,13) y palo en 'cptd'."""
        assert valor in self.VALORES
        assert palo in self.PALOS             
        self.num_carta = self.PALOS.index(palo)*13 + (valor - 1)
        
    def palo(self):
        """Devuelve el palo de la carta
        in: Una carta
        out: Un valor de palo
		pos: El valor del palo es un carácter del conjunto {cdtp}."""
        return self.PALOS[self.num_carta // 13]

    def valor(self):
        """Devuelve el valor de la carta
        in: Una carta
        out: Un valor de palo
		pos: El valor de la carta está en el rango (1-13)."""
        return self.num_carta % 13
    
    def nombrePalo(self):
        """Devuelve el nombre del palo de la carta
        in: Una carta
        out: El nombre del palo de la carta
        pos: El nombre es uno del conjunto {'corazones', 'picas', 'tréboles', 
		     'diamantes'}."""
        return self.NOMBRES_PALOS[self.num_carta // 13]
    
    def nombreValor(self):
        """Devuelve el nombre del valor de la carta
        in: Una carta
        out: El nombre del valor de la carta
        pos: El nombre es uno del conjunto {'as', 'dos', 'tres', ..., 'jack', 
		    'queen', 'rey'}."""
        return self.NOMBRES_VALORES[self.num_carta % 13]
    
    def __str__(self):
        """Devuelve la representación en cadena de la carta
        in: Una carta
        out: Una cadena con el nombre de la carta."""
        return '{0} de {1}'.format(self.nombreValor(), self.nombrePalo())