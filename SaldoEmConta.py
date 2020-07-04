# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:58:42 2020

@author: Lucas
"""
saldo=float(input("Digite o saldo: "))
if saldo < 0:
    print("\nSeu saldo atual é negativo: R$",saldo)
elif saldo > 0:
    print("\nSeu saldo atual é: R$",saldo)
else:
    print("\nNão há saldo no momento: R$",saldo)