#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[10]:


s = "\nДанила Корзюков \nИстратов Женя \nДэвид Тарасов"
print(re.findall(r'(?<=\n)\w+', s))

