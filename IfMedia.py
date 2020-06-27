# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:43:57 2020
@author: luksp
"""

#Entrada de dados
nota1=float(input('Digite a nota 1: '))
nota2=float(input('Digite a nota 2: '))
nota3=float(input('Digite a nota 3: '))
nota4=float(input('Digite a nota 4: '))

#Processamento de dados
soma=nota1+nota2+nota3+nota4
media=soma//4

if media >= 7.0:
    print('APROVADO')
else:
    print('REPROVADO')
    
print('NOTA FINAL',media)
