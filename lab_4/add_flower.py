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
    parser.add_argument('--stem_length', required=True, type=int)
    parser.add_argument('--with_thorns', default=False, action='store_true')
    parser.add_argument('--companion_plants', nargs='+')

    return parser

if __name__ == '__main__':
    journals = []
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    with open('journal.txt', '+') as file:
        journal = {
                    "name": namespace.name, "country": namespace.country, "stem-length": namespace.stem_length,
                    "with-thorns": namespace.with_thorns, "companion-plants": namespace.companion_plants
                }
        journals.append(journal)
        json.dump(journals, file, indent=4)


# In[ ]:





# In[ ]:




