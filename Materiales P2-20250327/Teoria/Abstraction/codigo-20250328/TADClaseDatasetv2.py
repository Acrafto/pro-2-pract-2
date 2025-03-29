# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:38:34 2019

@author: Mariano
"""

#TADClaseDatasetv2.py
from math import sqrt, pow
class Dataset:
    """Dataset es una colección de números a partir de los cuales
        calcular estadísticas descriptivas."""

    def __init__(self):	
        """Crea un dataset vacío
        out: Un nuevo dataset
        pos: El dataset no contiene datos."""
        self._max = self._min = None
        self._tamaño = self._suma = self._suma_cuadrados = 0

    def add(self, x):	
        """Añadir el elemento x al dataset
        in: Un dataset (self) y un elemento
        out: EL elemento x añadido al dataset"""
        if self._max == None:
            self._min = x
            self._max = x
        elif x > self._max:
            self._max = x
        elif x < self._min:
            self._min = x
        self._tamaño += 1
        self._suma += x
        self._suma_cuadrados += pow(x, 2)
                
    def min(self):
        """Devolver el valor mínimo del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 1
        pos: devuelve el valor más pequeño en self."""
        assert self._tamaño > 0
        return(self._min)

    def max(self):
        """Devolver el valor máximo del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 1
        pos: devuelve el valor más grande en self."""
        assert self._tamaño > 0
        return(self._max)
        
    def tamaño(self):
        """Calcula el tamaño del dataset
        in: Un dataset (self)
        out: Un valor entero."""
        return(self._tamaño)
        
    def media(self):
        """Calcula el valor medio del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 1."""
        assert self._tamaño > 0
        return(self._suma/self._tamaño)

    def desv_estandar(self):
        """Calcula el valor de la desviación estándar del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 2."""
        assert self._tamaño > 1
        return(sqrt((self._suma_cuadrados - (pow(self._suma,2)/self._tamaño))/(self._tamaño-1)))