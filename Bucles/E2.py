# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:47:42 2017

@author: USUARI

2. Crear una expresión que calcula el promedio de una colección de enteros
introducidos por el usuario. El usuario ingresará 0 como un valor de centinela
para indicar que no se proporcionará ningún valor adicional.
"""
suma = 0;
nums = 0;
n = int(raw_input("Nombre: "))

while n != 0:
    suma += n
    nums = nums + 1
    n = int(raw_input("Nombre: "))
print"Promig dels nombres introduits: ", str((suma/nums))