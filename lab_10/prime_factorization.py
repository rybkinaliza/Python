#!/usr/bin/env python
# coding: utf-8

# In[1]:


from multiprocessing import Pool
import argparse


# In[5]:


def factorize(n):
    divider = 2
    all_dividers = []
    while n != 1:
        while n % divider == 0:
            n = n / divider
            all_dividers.append(divider)
        divider += 1
    return all_dividers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', type=int, nargs='+')
    numbers = vars(parser.parse_args())['integers']
    
    with Pool() as p:
        factorized = p.map(factorize, numbers)

    for pair in zip(numbers, factorized):
        print(f'{pair[0]}:', *pair[1])


# In[ ]:




