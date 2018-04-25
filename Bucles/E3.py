# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:35:24 2017

@author: USUARI

3. Crear una expresión que calcula el valor máximo y mínimo de una colección
de enteros introducidos por el usuario.
"""

llista = []
nmax = int(raw_input("Quants nombres vols inserir? "))

for x in range(nmax):
    num = int(raw_input("Nombre: "))
    llista.append(num)
    
maxim = max(llista)
minim = min(llista)
print"Num. maxim: ", maxim, " / Num. minim: ", minim