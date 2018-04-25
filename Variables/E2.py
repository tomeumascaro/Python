# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:02:36 2017

@author: USUARI

2. Escribe una secuencia de instrucciones que permitan leer un número real
y muestre si el número está entre en el rango ( -1.0 ,y 1.0 ).
"""

nreal = float(raw_input("Introdueix nombre: "))

if nreal > -1.0 and nreal < 1.0:
    print"El nombre esta entre -1.0 i 1.0"
else:
    print"El nombre no esta entre -1.0 i 1.0"