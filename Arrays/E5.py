# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 19:46:07 2017

@author: USUARI

1)Crea dos matrices con contenido aleatorio, llamadas m y n.
2)Multiplicalas elemento a elemento.
3)Realiza la multiplicación de matrices.
4)Realiza la siguiente operación: ((m+n)*(-m/2))
5)Realiza la suma de los elementos de la diagonal de la matriz m.
6)Calcula el determinante de la matriz n.
"""

import numpy as np

#%% 1
m = np.array([[1., 2.], [4., 5.]]) #matriu (2, 2)
n = np.array([[6., 23.], [-1, 7]]) #matriu (2, 2)
print m
print n

#%% 2
if m.shape != n.shape:
    print "ERROR: No es pot multiplicar element a element si les matrius no tenen la mateixa dimensio"
else:
    multelem = np.multiply(m,n) #m*n element a element
    print "Resultat:"
    print multelem

#%% 3
multmatrix = np.dot(m,n) #m*n matricial
print "Resultat:"
print multmatrix

#%% 4
if m.shape != n.shape:
    print "ERROR: No es pot operar si les matrius no tenen la mateixa dimensio"
else:
    operacio = (np.dot((m+n),(np.divide(-m,2))))
    print "Resultat:"
    print operacio
    
#%% 5
diagonal = np.diag(m) #diagonal de m
suma = sum(diagonal)
print "Resultat: %i" %suma

#%% 6
determinant = np.linalg.det(n)
print "Resultat:"
print determinant