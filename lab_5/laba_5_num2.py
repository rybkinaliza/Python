#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random


# In[29]:


class Human:
    def __init__(self, name, sex, year_of_birth, hair_length, nail_length, nail_color = 'бесцветные'):
        self.name = str(name)
        self.sex = str(sex)
        self.year_of_birth = int(year_of_birth)
        self.hair_length = int(hair_length)
        self.nail_length = int(nail_length)
        self.nail_color = str(nail_color)

    def __str__(self):
        return f'Меня зовут {self.name}, теперь у меня волосы длины {self.hair_length} и {self.nail_color} ногти длины {self.nail_length}'  
        
class Stylist:
    def __init__(self, name, sex, year_of_birth):
        self.name = str(name)
        self.sex = str(sex)
        self.year_of_birth = int(year_of_birth)

nail_color = ['красные', 'фиолетовые', 'зелёные']
        
class Manicurist(Stylist):
    def __init__(self, name, sex, year_of_birth):
        super().__init__(name, sex, year_of_birth)
        
    def do_job(self, other):
        if other.nail_length > 1:
            other.nail_length = other.nail_length - 1
        other.nail_color = random.choice(nail_color)
        
class Hairdresser(Stylist):
    def __init__(self, name, sex, year_of_birth):
        super().__init__(name, sex, year_of_birth)
        
    def do_job(self, other):
        if other.hair_length > 1:
            other.hair_length = other.hair_length - 1

class Barber(Stylist):
    def __init__(self, name, sex, year_of_birth):
        super().__init__(name, sex, year_of_birth)
        
    def do_job(self, other):
        if other.sex == 'М':
            if other.hair_length > 1:
                other.hair_length = other.hair_length - 1
        else:
            raise ValueError
            
neo = Human(name="Neo", sex="M", year_of_birth=1964, hair_length=10, nail_length=2)
trinity = Human(name="Trinity", sex="F", year_of_birth=1967, hair_length=30, nail_length=5)

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)

manicurist.do_job(neo)
barber.do_job(neo)
barber.do_job(trinity)

print(neo)
print(trinity)


# In[ ]:





# In[ ]:




