#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[45]:


s = "Я сейчас читаю «Случайную вакансию» Джоан Роулинг.Не знаю, как тебе, а мне книга «Террор» Симмонса показалась очень затянутой.Конечно, я читал Гарри Поттера! Но вот фильм «Гарри Поттер и Кубок огня» мне совершенно не понравился!"
print(re.findall(r'(?<=читаю «)[\w\s]+(?=»)|(?<=книга «)[\w\s]+(?=»)|(?<=читал )[\w\s]+', s))

