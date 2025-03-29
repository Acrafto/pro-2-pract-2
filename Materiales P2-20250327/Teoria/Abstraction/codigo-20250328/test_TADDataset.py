# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:20:03 2019

@author: mariano
"""

# test_TADDataset.py
# Programa de prueba del TAD Dataset
from TADClaseDataset import Dataset

def main():
	print ('Programa para cálcular el min, max, media y desviación típica de un dataset.')
	data = Dataset()
	while True :
		xStr = input ('Introducir un número (<Entrar> para terminar): ')
		if xStr == '':
			break
		data.add(float(xStr))
	print ('Resumen de ', data.tamaño(), ' notas.')
	print ('Mínimo: ' , data.min())
	print ('Máximo: ' , data.max())
	print ('Media: ' , data.media())
	print ('Desviación típ.: ' , data.desv_estandar())
if __name__ == '__main__':
	main ()