#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[5]:


s = "Данила Корзюков Истратов Женя Дэвид Тарасов"
print(re.findall(r'\b\w{6}\b|\b\w{4}\b|\b\w{5}\b', s))


# In[ ]:




