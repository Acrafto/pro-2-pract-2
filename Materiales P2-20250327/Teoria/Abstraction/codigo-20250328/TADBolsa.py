# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:58:17 2019

@author: Mariano
"""
#TADBolsa.py
# Implementa el contenedor TAD Bolsa usando una lista.
class Bolsa:
    def __init__( self ):
        """Crear una bolsa vacía
        out: Una nueva bolsa
		pos: La bolsa no contiene elementos."""
        self._theItems = list()

    def add( self, item ):
        """Añade un item a la bolsa
        in: Una bolsa
        out: El item añadido a la bolsa"""
        self._theItems.append( item )

    def __len__( self ):
        """Devuelve el número de ítems en la bolsa.
        in: Una bolsa
        out: Un valor entero."""
        return len( self._theItems )

    def __contains__( self, item ):
        """Determina si el ítem esta en la bolsa.
        in: Una bolsa
        out: Un valor booleano
        pos: devuelve True si se encuentra, False en otro caso."""
        return item in self._theItems

    def __iter__( self ):
        """Crea un iterador para iterar sobre la bolsa
		pos: devuelve un iterador."""
        return _BolsaIterador( self._theItems )

    def remove( self, item ):
        """Elimina una ocurrencia de item en la bolsa. Se lanza una
		excepción si el elemento no se encuentra
        in: Una bolsa 
        out: La bolsa sin la ocurrencia de item
		pre: al menos hay una ocurrencia del item
        pos: el número de ocurrencias de item disminuye en uno """
        assert item in self._theItems, "El ítem debe estar en la lista."
        ndx = self._theItems.index( item )
        return self._theItems.pop( ndx )


# An iterator for the Bag ADT implemented as a Python list.
class _BolsaIterador :
	def __init__( self, theList ):
		self._bagItems = theList
		self._curItem = 0

	def __iter__( self ):
		return self

	def __next__( self ):
		if self._curItem < len( self._bagItems ) :
			item = self._bagItems[ self._curItem ]
			self._curItem += 1
			return item
		else:
			raise StopIteration
