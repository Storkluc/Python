# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:04:14 2020

@author: Lucas Oliveira

Desafio
"""

import numpy as np

#Construção de uma matrix 6x6 com um array
print('\n\n\n### Desafio Matriz 6x6 ### \n')
arr = np.array([np.arange(0,6),np.arange(10,16),np.arange(20,26),
                np.arange(30,36),np.arange(40,46),np.arange(50,56)])
print(arr,'\n')

#Slice de 3 e 4
print('',arr[0,3:5],'\n')

#Slice 20,22,24,40,42,44
print('',arr[2,0:6:2])
print('',arr[4,0:6:2],'\n')

#Slice 44,45,54,55
print('',arr[4,4:6],'\n',arr[5,4:6],'\n')

#Slice 2,12,22,32,42,52
print('',arr[0,2:3],'\n',arr[1,2:3],'\n',arr[2,2:3],'\n',arr[3,2:3],'\n',
      arr[4,2:3],'\n',arr[5,2:3])
