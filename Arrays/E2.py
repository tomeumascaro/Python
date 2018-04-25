# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:04:22 2017

@author: USUARI

1. Crea un array con los valores entre 10 y 50.
2. Crea una matriz de 3x3 con los valores de 0 a 8.
3. Crea la matriz identidad de 5x5.
4. Crea un array de 12 elementos y transformalo en una matriz de 4x3.
5. Crear un array de 10 elementos con los valores entre 0 y 1 espaciados uniformemente.
"""

import numpy as np

#%% 1
print np.arange(10,51,1)

#%% 2
print np.arange(0,9,1).reshape(3,3)

#%% 3
print np.eye(5)

#%% 4
print np.arange(12).reshape(4,3)

#%% 5
print np.linspace(0,1,10)