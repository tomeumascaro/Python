# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:39:23 2017

@author: USUARI

1.Construye un diccionario que permita traducir de texto a código morse,
luego construye una función que dado un string devuelva el correspondiente
código morse.
"""

morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':"."}

text = raw_input("Introdueix text: ")
resultat = ""

#traduim de text a codi morse
for i in text:
    resultat += morse[i]

print text, " = ", resultat

#funcio que retorna el codi morse d'un string
def string_morse(s):
    resultat2 = ""
    for i in s:
        resultat2 += morse[i]
    return resultat2

print text, " = ", string_morse(text)
