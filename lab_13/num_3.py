#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[ ]:


df_games = pd.read_csv('/Users/serik/games001.csv', sep=';')
df_rates =  pd.read_csv('/Users/serik/rates001.csv', sep=';')

df = df_games.copy() 

df['mean_rating'] = [round(df_rates[(df_rates['id'] == id)]['mark'].mean(), 3) for id in df['id']]
df1 = df.sort_values(by ='mean_rating', ascending=False).iloc[0:3][['name', 'mean_rating']].to_string(index=False)
print(df1)

df['rating_sum'] = [df[df['company'] == company]['mean_rating'].sum() for company in df['company']]
df2 = df.sort_values(by ='rating_sum', ascending=False).iloc[0:1][['company', 'rating_sum']].to_string(index=False)
print(df2)

