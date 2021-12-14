#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import sys
import threading
import argparse
from os.path import isfile, join
from os import listdir


# In[4]:


def thread_job(file, string):
    all_lines = []
    with open(file, 'r') as book:
        for line in book:
            if string in line:
                all_lines.append(line)
    return (print(f'{file}:', line))

def Parser():
    parser  = argparse.ArgumentParser()
    parser.add_argument("str", nargs = "+")
    return parser        

if __name__=='__main__':
    parser = Parser()
    string_input = parser.parse_args()
    
    if string_input.string:
        file_path = string_input.string.pop()
        thestring = ' '.join(map(str, string_input.string))
        print(thestring)
    
    threads = [
        threading.Thread(target=thread_job, args=(i,))
        for i in range(len(books))
    ]
    for thread in threads:
        thread.start()  
    for thread in threads:
        thread.join()  


# In[ ]:




