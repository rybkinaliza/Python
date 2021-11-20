#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Human:
    def __init__(self, name, sex, year_of_birth):
        self.name = str(name)
        self.sex = str(sex)
        self.year_of_birth = int(year_of_birth)

class Movie:
    def __init__(self, title, director, year, country, duration, age_limit):
        self.title = str(title)
        self.director = str(director)
        self.year = int(year)
        self.country = str(country)
        self.duration = int(duration)
        self.age_limit = int(age_limit)
        
    def is_allowed(self, other):
        if (2021 - other.year_of_birth) >= self.age_limit:
            return 'True'
        else:
            return 'False'
            
class Cartoon(Movie):
    def __init__(self, title, director, year, country, duration, age_limit, technique):
        super().__init__(title, director, year, country, duration, age_limit)
        self.technique = technique
        
class Anime(Cartoon):
    def __init__(self, title, director, year, country, duration, age_limit, technique):
        super().__init__(name = name, director = director, year = year, 
                         country = 'Japan', duration = duration, age_rating = age_rating, technique = 'drawn')
        
movie = Movie(
  title="Dune", director="Denis Villeneuve", year=2021,
  country="USA", duration=155, age_limit=13
)
human = Human(name="Neo", sex="M", year_of_birth=1964)

print(movie.is_allowed(human))


# In[ ]:




