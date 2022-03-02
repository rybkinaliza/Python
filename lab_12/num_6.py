#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


N=100
x_0=1


# In[10]:


ns = np.arange(1, N+1)
def Taylor(x_0, n):
    return ((-1)**(n+1))*(x_0**n)/n
res = Taylor(x_0, ns).sum()
print(res)

