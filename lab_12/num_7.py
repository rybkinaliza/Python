#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


X = np.array([[175, 4], [20, 2], [25, 8]]) # 1 столбец - 1 признак
X


# In[3]:


sums = X.sum(axis=0) #логично смотреть среднее по одному признаку
m=1
m, n = X.shape
mean = sums/m
print('sample mean:', mean)


# In[4]:


dev = X - np.reshape(np.repeat(mean, m), (n,-1)).T #deviation from mean
Q = np.dot(dev.T, dev)/(m-1)
print('sample covariation:\n', Q)

