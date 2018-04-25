# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:50:26 2017

@author: USUARI

4. Crear una expresión que calcula el mcd de dos números enteros
introducidos por el usuario.
"""

import math

a = int(raw_input("Nombre a: "))
b = int(raw_input("Nombre b: "))

while a > 0:
    aux = a
    a = math.fmod(b,a)
    b = aux
print"MCD (a,b): ", b