# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:10:52 2017

@author: USUARI

1.Crea una matriz de 3x3 con números aleatorios llamada m.
Ayuda: np.random.random((int,int))
2.Imprime el máximo de m. Imprime su mínimo. Imprime el máximo de la tercera
columna. Imprime el mínimo de la segunda fila.
3.Normaliza los valores de m para que estén entre 5 y 10.
4.Substituye todos los valores de m menores a 0.5 por 0.
5.Dado un array con todos los valores entre 1 y 11, niega todos los valores
entre 3 y 8.
6.Calcula su media sin usar la función mean tal como lo haríamos ayer.
Comprueba el resultado usando la función np.mean
7.Crea un array de 10 posiciones cuyos valores sean generados de forma
aleatoria basado en una distribución normal con media 0 y desviación típica 5.
"""

import numpy as np

#%% 1
m = np.random.randint(0,50,(3,3))
print m

#%% 2
print "MAX: ", np.max(m)
print "MAX 3a columna: ", np.max(m[:,2])
print "MIN 2a fila: ", np.min(m[2])

#%% 3
for i in range(0,m.shape[0]):
    for j in range(0,m.shape[1]):
        if m[i,j] < 5 or m[i,j] > 10:
            m[i,j] = np.random.randint(5,10)
print m