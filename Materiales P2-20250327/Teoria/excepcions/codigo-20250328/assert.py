# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:07:02 2020

@author: Mariano
"""

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(KelvinToFahrenheit(-5))

