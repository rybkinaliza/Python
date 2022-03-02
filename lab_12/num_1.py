#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def f(x):
    return np.sin(x/5)*np.exp(x/10) + 5*np.exp(-x/2)


# In[4]:


x = np.array([1, 4, 10, 15])
A = np.array([[1, 1, 1, 1], x, x**2, x**3]).T
b = f(x)
w = np.linalg.solve(A, b)
w


# In[7]:


k = np.linspace(1, 15, 1000)

plt.figure(figsize=(7,5))
plt.plot(k, f(k))
plt.minorticks_on()
plt.grid(which='major',
        color = 'k', 
        linewidth = 1)
plt.grid(which='minor', 
        color = 'k', 
        linestyle = ':')

plt.plot(k, w[0]+w[1]*k+w[2]*k**2+w[3]*k**3)

