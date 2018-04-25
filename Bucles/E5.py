# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:57:57 2017

@author: USUARI

5. Crear una expresión que guarde en una lista todos los valores múltiplos
de 5 o 7 entre 3000 y 5000. Muestra dicha lista por pantalla, cada valor debe
estar en una línea separada.
"""
llista = []

for i in range(3000,5000):
    if i%5 == 0 or i%7 == 0:
        llista.append(i)

for i in llista:
    print i