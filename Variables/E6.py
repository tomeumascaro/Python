# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:37:09 2017

@author: USUARI

6. Escribe una secuencia de instrucciones para averiguar si un número
natural m, leído del teclado, es un cuadrado perfecto, o sea, si es de la
forma m = n2 para algún natural n.
"""

m = int(raw_input("Nombre m: "))
n = 0

while n <= m:
    if m == n*n:
        print("El nombre m es quadrat perfecte de " + str(n))
        m = -1 #Actualitzam m per sortir del bucle
    else:
        n = n + 1