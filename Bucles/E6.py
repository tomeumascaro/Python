# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:07:11 2017

@author: USUARI

6. Crear una expresión que dada la lista de nombres noms (ver PaP anterior)
cambie la primera y la última letra de cada nombre por la letra ‘s’.
"""

noms = ['juan', 'jordi', 'jesus', 'joan', 'jaume', 'jose']

for i in range(len(noms)):
    cadena = noms[i]
    cadena_nova = 's' + cadena[1:len(cadena)-1] + 's'
    print cadena_nova