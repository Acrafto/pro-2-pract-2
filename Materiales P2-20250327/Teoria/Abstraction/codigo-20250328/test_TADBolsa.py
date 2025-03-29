# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:13:53 2020

@author: Mariano
"""
# test_TADBolsa
from TADBolsa import Bolsa

def main():
    print('Implementación del carro de la compra')
    print(' usando un TAD Bolsa.')
    
    # Sacar la bolsa
    bolsa = Bolsa()

    # Hacer la compra
    while True:
        articulo = input('Articulo (. fin): ')
        if articulo =='.':
            break
        unidades = int(input('Unidades: '))
        precio = float(input('Precio: ' ))
        for i in range(0,unidades):
            bolsa.add((articulo, precio))
    
    # Devolver una unidad de un producto de la bolsa
    print('\nDevolución------')
    articulo = input('Articulo (. fin): ')
    precio = float(input('Precio: ' ))
    bolsa.remove((articulo, precio))
    
    # Paso por caja
    total = 0
    print('\nEn caja---------')
    for item in bolsa:
        print('Articulo: {0}\t{1}'.format(item[0], item[1]))
        total += item[1]

    # A pagar
    print('TOTAL: {0:5.2f}'.format(total))

if __name__ == '__main__':
	main ()    