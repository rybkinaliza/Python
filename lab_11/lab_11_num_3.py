#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[15]:


s = '''def print_hello(): 
print("Hello!")
class Goodbyer:
def print_goodbye(self):
print('Bye!')'''
print(re.findall(r'(?<=def).+\s+.+', s))

