# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:33:06 2020

@author: Mariano
"""

# excepciones_definidas_usuario.py
# Definición y manejo de excepciones definidas por usuario

class Error(Exception):
   """Base class for other exceptions"""
   pass

#Define class for NegativeValueError
class ErrorValorNegativo(Error):
  """Raised when the input is negative"""
  pass

#Define class for ValueTooSmallError
class ErrorValorMuyPequeno(Error):
   """Raised when the value is too small"""
   pass

#Define class for ValueTooLargeError
class ErrorValorMuyGrande(Error):
   """Raised when the value is too large"""
   pass

# main program
# Takes input till the user inputs correct value
number = 11

while True:
   try:
       num = int(input("Número: "))
       if num < 0:
           raise ErrorValorNegativo
       elif num < number:
           raise ErrorValorMuyPequeno
       elif num > number:
           raise ErrorValorMuyGrande
       break
   except ErrorValorNegativo:
       print("¡Valor negativo!")
       print("")
   except ErrorValorMuyPequeno:
       print("¡Valor demasiado pequeño!")
       print("")
   except ErrorValorMuyGrande:
       print("¡Valor demasiado grande!")
       print("")
print("Valor correcto")