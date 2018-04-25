# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:26:11 2017

@author: USUARI

4. Escribe una secuencia de instrucciones que permitan leer dos números
enteros y muestre el cociente de la división y el resto.
"""

x = int(raw_input("Introdueix primer nombre: "))
y = int(raw_input("Introdueix segon nombre: "))

quocient = x/y
resto = x%y

print("Quocient: " + str(quocient))
print("Residu: " + str(resto))