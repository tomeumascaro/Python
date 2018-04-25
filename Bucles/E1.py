# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:37:44 2017

@author: USUARI

1. Escribe una expresión que muestre una tabla de conversión de temperatura
para grados Celsius y grados Fahrenheit. La tabla debe incluir filas para
todas las temperaturas entre 0 y 100 grados Celsius que son múltiplos de
10 grados Celsius.
"""

for x in range(101): #de 0 a 100
    print "Graus:      ", int(x)
    print "Farenheits: ", int(x+273)