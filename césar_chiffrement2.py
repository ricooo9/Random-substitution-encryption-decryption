# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:31:09 2023

@author: Foulie Aymeric
"""
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input('Entrez votre message à coder en minuscule : ')

clé_privé=alphabet.copy()
random.shuffle(clé_privé)
message_codé=''

for lettres in message :
    if not lettres in alphabet :
        message_codé+=lettres
    else :
        position = alphabet.index(lettres)
        message_codé+=str(clé_privé[position])

clé_privé = ''.join(clé_privé)
print("Le message codé est : ",message_codé)
print("Sa clé privée est : ", clé_privé)
