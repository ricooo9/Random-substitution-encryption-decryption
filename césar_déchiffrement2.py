# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:21:49 2023

@author: Foulie Aymeric
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = input('Entrez votre message à décoder en minuscule : ')
clé = input('Entrez votre clé privée : ')
clé_finale=[]
for i in clé:
    clé_finale.append(i)
message_décodé=[]

for lettre in message :
    if lettre not in alphabet :
        message_décodé.append(lettre)
    else :
        position = clé_finale.index(lettre)
        nvlettre = alphabet[position]
        message_décodé.append(nvlettre)

message_décodé = ''.join(message_décodé)    
print("Le voici le message décrypté avec votre clé privée : ",message_décodé)