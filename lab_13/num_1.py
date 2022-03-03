#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


N, M = map(int, (input().split()))
map_data = [np.array(((input().split())), dtype = int) for _ in range(N)]
df = pd.DataFrame(map_data)


# In[8]:


print(((df < -5).astype(int)).values.sum())
print(abs(int(df[df < 0].fillna(0).values.sum())))
print(df.values.max())


# In[ ]:




