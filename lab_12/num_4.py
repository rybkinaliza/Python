#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.array([2, 0, 0, 5, 8, 0, 6])


# In[3]:


print(max((x[i] for i in range(1, len(x)) if x[i - 1] == 0), default=None))

