# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:43:57 2017

@author: USUARI
"""

import numpy as np

#%%
llista = [1,2,3,4]
arr = np.array(llista, dtype='int8')

print arr

#%%
arr0 = np.zeros((4,4))
arr1 = np.ones((3,3))
print arr0
print arr1

#%%
arr123 = np.arange(5)
print arr123
arr1234 = np.arange(2,4,0.2)
print arr1234
arr123456 = np.arange(2,4.3,0.2).reshape(3,4)
print arr123456

#%%
arrsep = np.linspace(1.,5.,8)
print arrsep

#%%
arrid = np.eye(4)
print arrid