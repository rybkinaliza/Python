#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json


# In[18]:


def pluz(arg1, arg2):
    try:
        s = arg1 + arg2
    except TypeError:
        s = int(arg1) + int(arg2)
    return s


# In[ ]:




