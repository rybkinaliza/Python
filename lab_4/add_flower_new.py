#!/usr/bin/env python
# coding: utf-8

# In[18]:


import argparse
import json


# In[19]:


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--name', required=True, type=str)
    parser.add_argument('--country', required=True, type=str)
    parser.add_argument('--petal_colour', required=True, type=str)
    parser.add_argument('--stem_length', required=True, type=int)
    parser.add_argument('--with_thorns', default=False, action='store_true')
    parser.add_argument('--companion_plants', nargs='+')

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    with open("journal.txt", "a") as output_file:
    args = vars(parser.parse_args())
    json.dump(args, output_file)


# In[ ]:





# In[ ]:




