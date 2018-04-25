# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:06:39 2017

@author: USUARI

3. Escribe una secuencia de instrucciones que permitan leer las coordenadas de
un punto (x, y) e indique en el cuadrante en el que se encuentra dicho punto.
"""

#%%
x = float(raw_input("Introdueix coordenada X: "))
y = float(raw_input("Introdueix coordenada Y: "))

#%%
if x >= 0.0 and y >= 0.0:
    print"Quadrant 1"
elif x < 0.0 and y >= 0.0:
    print"Quadrant 2"
elif x < 0.0 and y < 0.0:
    print"Quadrant 3"
else:
    print"Quadrant 4"