# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:58:42 2020

@author: luksp
"""

import numpy as np

#Array com 10 zeros
arr = np.zeros((1,10))
print('\n\n',arr,'\n')

#Array com 10 números 1
arr = np.ones((1,10))
print('',arr,'\n')

#Array com 10 números 5
arr = [5 for i in range(10)]
print('',arr,'\n')

#Array entre 15 e 150
arr = np.arange(15,151)
print('',arr,'\n')

#Array de números negativos
arr = np.arange(10,51)
arr = [arr[i]*-1 for i in range(41)]
print('',arr,'\n')

#Matriz com distribuição gaussiana
arr = np.random.normal(0,1,(3,3))
print('',arr,'\n')





