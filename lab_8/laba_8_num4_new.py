#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List, Optional
import random


# In[5]:


class RandomChoiceIterator:
    def __init__(self, values: List[int], num_iters: Optional[int] = None):
        self.values = values
        self.num_iters = num_iters
        self.num_iterations = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num_iters is not None and self.num_iterations >= self.num_iters:
            raise StopIteration
            
        self.num_iterations += 1
        return random.choice(self.values)
            
            
for value in RandomChoiceIterator([1, 2, 3], num_iters = 5):
    print(value)


# In[ ]:




