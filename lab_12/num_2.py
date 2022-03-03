#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[2]:


x = np.array([1, 5, 1, 1, 0, 1, 1])
y = np.array([0, 2, 0, 2, 0, 2, 0])


# In[3]:


x_log = (x!=0)
y_log = (y!=0)
x_log, y_log


# In[5]:


print(f'Количество позиций, где оба не 0: ', np.logical_and(x_log, y_log).sum())
print(f'Количество позиций, где хотя бы один не 0: ', (x_log + y_log).sum())

