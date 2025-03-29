# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:57:00 2019

@author: mariano
"""
# TADClaseCarta.py
    
class Carta:
    """Un simple juego de cartas. Una carta se caracteriza por dos componentes.
	valor: un valor entero en el rango 1-13 incluido (As-Rey)
	palo: un carácter de 'cptd' correspodiente a corazones, picas,
	      tréboles, diamantes."""
          

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
        self.valor_num = valor
        self.palo_char = palo
        
    def palo(self):
        """Devuelve el palo de la carta
        in: Una carta
        out: Un valor de palo
		pos: El valor del palo es un carácter del conjunto {cdtp}."""
        return self.palo_char

    def valor(self):
        """Devuelve el valor de la carta
        in: Una carta
        out: Un valor de palo
		pos: El valor de la carta está en el rango (1-13)."""
        return self.valor_num
    
    def nombrePalo(self):
        """Devuelve el nombre del palo de la carta
        in: Una carta
        out: El nombre del palo de la carta
        pos: El nombre es uno del conjunto {'corazones', 'picas', 'tréboles', 
		     'diamantes'}."""
        return self.NOMBRES_PALOS[self.PALOS.index(self.palo_char)]
    
    def nombreValor(self):
        """Devuelve el nombre del valor de la carta
        in: Una carta
        out: El nombre del valor de la carta
        pos: El nombre es uno del conjunto {'as', 'dos', 'tres', ..., 'jack', 
		    'queen', 'rey'}."""
        return self.NOMBRES_VALORES[self.VALORES.index(self.valor_num)]
    
    def __str__(self):
        """Devuelve la representación en cadena de la carta
        in: Una carta
        out: Una cadena con el nombre de la carta."""
        return '{0} de {1}'.format(self.nombreValor(), self.nombrePalo())
    
    def __eq__(self, otra):
        """Comprueba si dos cartas son iguales
        in: Dos cartas
        out: Un valor booleano
        pos: Devuelve True si self y otra tienen mismo valor y palo, False en otro caso."""
        return self.palo_char == otra.palo_char and self.valor_num == otra.valor_num

    def __lt__(self, otra):
        """Comprueba si una carta es menor que otra, primero por palo y luego por valor
        in: Dos cartas
        out: Un valor booleano
        pos: Devuelve True si self es menor que la otra, False en otro caso."""
        t1 = self.palo_char, self.valor_num
        t2 = otra.palo_char, otra.valor_num
        return t1 < t2

    def __gt__(self, otra):
        """Comprueba si una carta es mayor que otra, primero por palo y luego por valor
        in: Dos cartas
        out: Un valor booleano
        pos: Devuelve True si self es mayor que la otra, False en otro caso."""
        t1 = self.palo_char, self.valor_num
        t2 = otra.palo_char, otra.valor_num
        return t1 > t2    