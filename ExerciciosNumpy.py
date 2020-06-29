# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:58:42 2020

@author: Lucas Oliveira
"""

import numpy as np

#Array com 10 zeros
arr = np.zeros((1,10))
print('\n\n','Array com zeros\n',arr,'\n')

#Array com 10 números 1
arr = np.ones((1,10))
print('','Array com números 1\n',arr,'\n')

#Array com 10 números 5
arr = [5 for i in range(10)]
print('','Array com números 5\n',arr,'\n')

#Array entre 15 e 150
arr = np.arange(15,151)
print('','Array com números entre 15 e 150\n',arr,'\n')

#Array de números negativos
arr = np.arange(10,51)
arr = [arr[i]*-1 for i in range(41)]
print('','Array com números negativos entre -10 e -50\n',arr,'\n')

#Matriz com distribuição gaussiana
arr = np.random.normal(0,1,(3,3))
print('','____Matriz com distribuição gaussiana___\n\n',arr,'\n')

#Soma colunas
soma = arr[0,0]+arr[1,0]+arr[2,0]
print(' Soma 1º coluna:', soma)
soma = arr[0,1]+arr[1,1]+arr[2,1]
print(' Soma 2º coluna:', soma)
soma = arr[0,2]+arr[1,2]+arr[2,2]
print(' Soma 3º coluna:', soma,'\n')

#Estatística

print('___Estatistica___\n\n Valor máximo:', arr.max())
print(' Valor mínimo:', arr.min())
print(' Media:', np.mean(arr))
print(' Desvio Padrão:', np.std(arr))
print(' Variância:',np.var(arr),'\n')




#Matriz de zeros envolto de 1s
arr = np.ones((5))
arr2 = np.ones((1))
arr3 = np.zeros((3))
arr4 = np.concatenate((arr2,arr3,arr2))
arr5 = np.array((arr,arr4,arr4,arr4,arr))
print(' Matriz 3x3\n',arr5)





