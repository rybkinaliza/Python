#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[ ]:


string_mat = input()
string_col = input()
X = input()
with open(string_mat) as A, open(string_col) as b:
    matrix_A = np.array([np.array((line.split()), dtype = float) for line in A])
    column_b = np.array([np.array((line.split()), dtype = float) for line in b]).T
    matrix_A2 = matrix_A @ matrix_A
    vector_X = np.array([np.array((X.split()), dtype = float)])
    print(round((vector_X @ matrix_A2 @ column_b)[0][0], 17))

