# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:38:34 2019

@author: Mariano
"""

#TADClaseDataset.py
from math import sqrt, pow
class Dataset:
    """Dataset es una colección de números a partir de los cuales
        calcular estadísticas descriptivas."""

    def __init__(self):	
        """Crea un dataset vacío
        out: Un nuevo dataset
        pos: El dataset no contiene datos."""
        self._data = []
        self._tamaño = 0

    def add(self, x):	
        """Añadir el elemento x al dataset
        in: Un dataset (self) y un elemento
        out: EL elemento x añadido al dataset"""
        self._data.append(x)
        self._tamaño += 1
        
    def min(self):
        """Devolver el valor mínimo del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 1
        pos: devuelve el valor más pequeño en self."""
        assert self._tamaño > 0        
        return(min(self._data))

    def max(self):
        """Devolver el valor máximo del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 1
        pos: devuelve el valor más grande en self."""
        assert self._tamaño > 0        
        return(max(self._data))
        
    def tamaño(self):
        """Calcula el tamaño del dataset
        in: Un dataset (self)
        out: Un valor entero."""
        return(len(self._data))
        
    def media(self):
        """Calcula el valor medio del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 1."""
        assert self._tamaño > 0        
        return(sum(self._data)/self._tamaño)

    def desv_estandar(self):
        """Calcula el valor de la desviación estándar del dataset
        in: Un dataset (self)
        out: Un valor real
        pre: El tamaño del dataset >= 2."""
        assert self._tamaño > 1        
        diferencias = 0
        _media = self.media()
        for i in self._data:
            diferencias += pow((i - _media), 2)
        return(sqrt(diferencias / (self._tamaño - 1)))