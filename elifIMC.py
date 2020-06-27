# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:05:40 2020
Pi
@author: luksp
"""

print('CALCULADORA IMC')
altura=float(input('Informe a sua altura: '))
peso=float(input('informe o seu peso: '))

imc=float (peso/(altura**2))

print('IMC: %d' %imc)
if imc<17:
    print('Muito abaixo do peso.')
elif imc<18.49:
    print('Abaixo do peso.')
elif imc<24.99:
    print('Peso normal')
elif imc<29.99:
    print('Acima do peso')
elif imc<34.99:
    print('Obesidade I')
elif imc<39.99:
    print('Obesidade II (severa)')
elif imc>40.00:
    print('Obesidade III(mórbida)')