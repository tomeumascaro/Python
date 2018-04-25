# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:34:19 2017

@author: USUARI

5. Escribe una secuencia de instrucciones que pidan el nombre del usuario y si
nos contestan que se llama Marta o Isaac nos conteste que es un nombre bonito,
si se llama de otra manera contestaremos que es un nombre normal.
"""

nom = raw_input("Introdueix un nom: ")

if nom == "Marta" or nom == "Isaac":
    print"Quin nom mes guapo!"
else:
    print"Nom normal"