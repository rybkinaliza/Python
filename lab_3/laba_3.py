#!/usr/bin/env python
# coding: utf-8

# In[56]:


import csv
import json
import os


# In[57]:


vitamins = []
for current_dir, dirs, files in os.walk("Vitamins"):
    with open('vitamin.json', 'w') as outfile:
        for vit in files:
            if vit.endswith(".txt"):
                file = open(vit, "r")
                vitamin = {
                    "vitamin": file.readline().rstrip('\n'),
                    "vitamers": file.readline().rstrip('\n'),
                    "solubility": file.readline().rstrip('\n'),
                    "daily_requirement": file.readline().rstrip('\n'),
                    "deficiency_diseases": file.readline()
                }
                vitamins.append(vitamin)
        json.dump(vitamins, outfile, indent=4)
    
vitamin_json = open('vitamin.json')
print(vitamin_json.read())


# In[59]:


for current_dir, dirs, files in os.walk("Vitamins"):
    with open("vitamin.csv", "w") as vitamin_csv:
        file_writer = csv.writer(vitamin_csv, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["vitamin", "vitamers", "solubility",
                                      "daily_requirement", "deficiency_diseases"])
        for vit in files:
            if vit.endswith(".txt"):
                file = open(vit, "r")
                file_writer.writerow([file.readline().rstrip('\n'), file.readline().rstrip('\n'),
                                      file.readline().rstrip('\n'), file.readline().rstrip('\n'),
                                     file.readline().rstrip('\n')])
vitamin_csv = open('vitamin.csv')
print(vitamin_csv.read())


# In[ ]:




