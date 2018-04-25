# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:58:02 2017

@author: USUARI

Dada la lista, noms = [“juan”, “jordi”, “jesus”, “joan”, “jaume”, “jose”]
1. Muestra la lista ordenada alfabeticamente.
2. Muestra la lista ordenada con el orden alfabético invertido.
3. Elimina a “jordi” de la lista.
4. Añade a “miquel” al final de la lista.
5. Substituye a “joan” por “toni”.
6. Substituye a “juan” por “joan”
7. Muestra por pantalla el último elemento de la lista.
8. Cuantos elementos tiene la lista ahora mismo?
9. Cuantas veces tenemos a “joan” en la lista?
10. Vacía la lista y muestra el resultado por pantalla
"""
#%% LLISTA
noms = ['juan', 'jordi', 'jesus', 'joan', 'jaume', 'jose']

#%% E1
print "Llista noms sense ordenar: ", noms
noms.sort(); #ordenam llista
print "Llista noms ordenada: ", noms

#%% E2
print "Llista noms sense ordenar: ", noms
noms.sort(); #ordenam llista
noms.reverse(); #giram llista
print "Llista noms ordenada inversament: ", noms

#%% E3
noms.remove('jordi')
print "Llista noms sense en Jordi: ", noms

#%% E4
noms.append('miquel')
print "Llista noms amb en Miquel afegit al final: ", noms

#%% E5
pos = noms.index('joan') #agafam posicio den joan
noms.pop(pos) #eliminam en juan
noms.insert(pos,'toni') #inserim toni on hi havia en joan
print "Llista substituint Joan per Toni: ", noms

#%% E6
pos = noms.index('juan') #agafam posicio den juan
noms.pop(pos) #eliminam en juan
noms.insert(pos,'joan') #inserim joan on hi havia en juan
print "Llista substituint Juan per Joan: ", noms

#%% E7
obj = noms[len(noms)-1]
print "Derrer element de la llista: ", obj

#%% E8
nelements = len(noms)
print "Num. elements de la llista: ", nelements

#%% E9
nvegades = noms.count('joan')
print "L'element joan apareix ", nvegades, " vegades"

#%% E10
noms = []
print "Llista buida: ", noms