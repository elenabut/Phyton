#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Задание 1
import numpy as np
n = int(input('Введите число N'))
arr1 = np.arange(0, n, 1)
arr2 = np.flip(arr1, axis = 0)
#print(arr1)
print(arr2)


# In[2]:


#Задание 2
arr3 = np.diag(arr2)
arr4 = np.trace(arr3)
print(arr3)
print(arr4)


# In[5]:


#Задание 3
a = [[4, 2, 1], 
     [1, 3, 0], 
     [0, 5, 4]]
b = [4, 12, -3]
from numpy import linalg
x = linalg.solve(a, b)
print(x)
np.dot(a, x)


# In[29]:


#Задание 4
# НЕ могу разобраться, в чем ошибка в 4-м задании?
users_stats = (
[[2, 1, 0, 0, 0, 0],
[1, 1, 2, 1, 0, 0],
[2, 0, 1, 0, 0, 0],
[1, 1, 2, 1, 0, 1],
[0, 0, 1, 2, 0, 0],
[0, 0, 0, 0, 0, 5],
[1, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 3],
[1, 0, 0, 2, 1, 4]],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

def cosine( users_stats, next_user_stats ):
    aLength = np.linalg.norm( users_stats )
    bLength = np.linalg.norm( next_user_stats )
    
    return np.dot( users_stats, next_user_stats ) / ( aLength * bLength )

np.array([cosine(row, next_user_stats) for row in users_stats])

