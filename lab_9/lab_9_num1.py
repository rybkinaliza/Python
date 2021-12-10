#!/usr/bin/env python
# coding: utf-8

# In[7]:


def calculator():
    elements_sum = 0
    elements_sq_sum = 0
    total = 0
    while True:
        element = yield
        total += 1
        elements_sum += element
        elements_sq_sum += element ** 2
        
        avarage = elements_sum / total
        avarage_sq = elements_sq_sum / total

        print(f'Среднее значение: {avarage}, дисперсия: {avarage_sq - avarage ** 2}, всего чисел: {total}')


coroutine = calculator()
next(coroutine)
for element in range(5):
    coroutine.send(element)

