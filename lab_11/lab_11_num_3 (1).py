#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re


# In[84]:


s = '''def print_hello():\n print("Hello!")\n class Goodbyer:\n def print_goodbye(self):\n print('Bye!')'''
print(re.findall(r'(?<='').+\s+.+(?=\n class)|(?<=:\n).+\s+.+', s))


# In[ ]:




