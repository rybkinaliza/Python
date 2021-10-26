#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[16]:


class Base:                
    def __eq__(self, other):
        return self.acid == other.acid

    def __ne__(self, other):
        return self.acid != other.acid

class RNA(Base):
    def __init__(self, acid):
        if not isinstance(acid, str):
            raise TypeError('Acid must be str type')
        if acid.count('A') + acid.count('U') +                 acid.count('G') + acid.count('C') != len(acid):
            raise Exception('Only nucliotides A, U, G, C must be in RNA')
        self.acid = acid
        return
    
    def __getitem__(self, item):
        return self.acid[item]
    
    def __add__(self, other):
        return RNA(self.acid + other.acid)
    
    def __mul__(self, other):
        sequence_1 = self.acid
        sequence_2 = other.acid
        if len(sequence_1) < len(sequence_2):
            sequence_1, sequence_2 = sequence_2, sequence_1
        result = ''
        for i in range(len(sequence_2)):
            if bool(randint(0, 1)):
                result += sequence_1[i]
            else:
                result += sequence_2[i]
        if len(sequence_1) != len(sequence_2):
            result += sequence_1[len(sequence_2)+1:]
        return RNA(result)

    def __repr__(self):
        return f'{self.acid} Class RNA'

    def __str__(self):
        return f'RNA: {self.acid}'


class DNA(Base):
    def __init__(self, acid):
        if not isinstance(acid, str):
            raise TypeError('Acid must be str type')
        if acid.count('A') + acid.count('T') +                 acid.count('G') + acid.count('C') != len(acid):
            raise Exception('Only nucliotides A, T, G, C must be in DNA')
        self.acid = acid
        acid2 = ''
        for i in range(len(acid)):
            if acid[i] == 'A':
                acid2 += 'T'
            elif acid[i] == 'T':
                acid2 += 'A'
            elif acid[i] == 'G':
                acid2 += 'C'
            elif acid[i] == 'C':
                acid2 += 'G'
        self.acid2 = acid2
        return

    def __getitem__(self, item):
        return self.acid[item] + '-' + self.acid2[item]
    
    def __add__(self, other):
        return DNA(self.acid + other.acid)

    def __mul__(self, other):
        sequence_1 = self.acid
        sequence_2 = other.acid
        if len(sequence_1) < len(sequence_2):
            sequence_1, sequence_2 = sequence_2, sequence_1
        result = ''
        for i in range(len(sequence_2)):
            if bool(randint(0, 1)):
                result += sequence_1[i]
            else:
                result += sequence_2[i]
        if len(sequence_1) != len(sequence_2):
            result += sequence_1[len(sequence_2)+1:]
        return DNA(result)

    def __repr__(self):
        return f'{[self.acid, self.acid2]} Class DNA'

    def __str__(self):
        return f'DNA: {[self.acid, self.acid2]}'

