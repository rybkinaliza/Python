#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.array([2, 0, 0, 5, 8, 0, 0, 6])


# In[13]:


x_modified = np.arange(len(x))
x_modified[x == 0] = 0
x_modified = np.maximum.accumulate(x_modified)
x[x_modified]

