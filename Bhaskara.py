# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:16:44 2020

@author: Lucas Oliveira
"""
import math

#Entrada de dados
print('___Bhaskara___')
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

#Resultado
delta=(b**2)-(4*a*c)
if delta > 0:
    x1=(-b+(math.sqrt(delta)))/(2*a)
    x2=(-b-(math.sqrt(delta)))/(2*a)
    print("\n-RESULTADO-\n\n X':",round(x1,2),'\n','X":',round(x2,2))
elif delta==0:
    x1=(-b-(math.sqrt(delta)))/(2*a)
    print("\n-RESULTADO-\n\nX':",round(x1,2))
else:
    print('Não é possível calcular raiz para o delta')
    