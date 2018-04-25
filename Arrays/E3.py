# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:35:37 2017

@author: USUARI

1.Crea un array de 10 posiciones con todos los valores del 8 al 17.
Substituye el quinto por un 1. Muéstralo por pantalla.
2.Crea una matriz de 10x10 posiciones con valor 1 en los bordes y valor 0
en el interior.
3.Crea una matriz de 5x3 posiciones con valores del 1 al 15, imprime la
segunda fila. Imprime la primera columna.
4.Crea una matriz de 5x5 posiciones con los valores de 0 a 24 y substituye
la quinta fila por el valor 5. Cuántos números son mayores que 10? Cuántos
son menores que 18?
"""

import numpy as np

#%% 1
a = np.linspace(8,17,10)
a[5] = 1
print a

#%% 2
a0 = np.zeros((10,10))
a0[0] = 1
a0[9] = 1
a0[:,0] = 1
a0[:,9] = 1
print a0

#%% 3
print np.arange(1,16).reshape(5,3)
print a[1] #2a fila
print a[:,0] #1a columna

#%% 4
a = np.arange(0,25).reshape(5,5)
a[4] = 5
print a

majors10 = a[a > 10]
menors18 = a[a < 18]
print "Nº > 10: ", len(majors10), " / Nº < 18: ", len(menors18)