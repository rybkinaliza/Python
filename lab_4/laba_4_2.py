#!/usr/bin/env python
# coding: utf-8

# In[32]:


def author(arg):
    def wrapper(func):
        func._author = arg
        return func
    return wrapper


@author("Dany Longo")
def add2(num: int) -> int:
    return num + 2


print(add2._author)


# In[ ]:




