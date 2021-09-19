#!/usr/bin/env python
# coding: utf-8

# In[12]:


transl_subseq = []
dictionary = {-1:' ', 0:'а', 1:'б', 2:'в', 3:'г', 4:'д', 5:'е', 6:'ё', 7:'ж', 8:'з', 9:'и', 10:'й', 
             11:'к', 12:'л', 13:'м', 14:'н', 15:'о', 16:'п', 17:'р', 18:'с', 19:'т', 20:'у', 21:'ф',
             22:'х', 23:'ц', 24:'ч', 25:'ш', 26:'щ', 27:'ъ', 28:'ы', 29:'ь', 30:'э', 31:'ю', 32:'я'}
subseq = input()
while subseq != "End":
    transl_subseq.append(dictionary[int(subseq)])
    subseq = input()
print(''.join(transl_subseq))


# In[ ]:




