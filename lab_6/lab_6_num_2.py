#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ValueError
        
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __repr__(self):
        return f'Rational({self.numerator}, {self.denominator})'
    
    def __add__(self, other):
        numerator = self.numerator*other.denominator + other.numerator*self.denominator
        denominator = self.denominator*other.denominator
        numerator_result, denominator_result = numerator, denominator
        while denominator != 0:
            numerator, denominator = denominator, numerator%denominator
        return Rational(numerator_result//numerator, denominator_result//numerator)
    
    def __sub__(self, other):
        numerator = self.numerator*other.denominator - other.numerator*self.denominator
        denominator = self.denominator*other.denominator
        numerator_result, denominator_result = numerator, denominator
        while denominator != 0:
            numerator, denominator = denominator, numerator%denominator
        return Rational(numerator_result//numerator, denominator_result//numerator)
    
    def __mul__(self, other):
        numerator = self.numerator*other.numerator
        denominator = self.denominator*other.denominator
        numerator_result, denominator_result = numerator, denominator
        while denominator != 0:
            numerator, denominator = denominator, numerator%denominator
        return Rational(numerator_result//numerator, denominator_result//numerator)
    
    def __truediv__(self, other):
        numerator = self.numerator*other.denominator
        denominator = self.denominator*other.numerator
        numerator_result, denominator_result = numerator, denominator
        while denominator != 0:
            numerator, denominator = denominator, numerator%denominator
        return Rational(numerator_result//numerator, denominator_result//numerator)
    
    def __float__(self):
        return self.numerator/self.denominator
    
    def from_string(string):
        all_num = string.split('/')
        n = int(all_num[0])
        m = int(all_num[1])
        return Rational(n, m)
    
    def __eq__(self, other):
        if self.numerator !=0 and other.numerator != 0:
            if self.numerator > other.numerator:
                z = self.numerator / other.numerator
            else:
                z = other.numerator / self.numerator
            if self.denominator > other.denominator:
                k = self.denominator / other.denominator
            else:
                k = other.denominator / self.denominator
            if z == k:
                return True
            else:
                return False
        elif self.numerator == other.numerator and other.numerator == 0:
            return True
        else:
            return False


def test_operations():
    assert Rational(1, 2) + Rational(1, 2) == Rational(1, 1)
    assert Rational(1, 2) - Rational(1, 2) == Rational(0, 1)
    assert Rational(1, 2) * Rational(-1, 2) == Rational(-1, 4)


def test_cast_to_float():
    assert float(Rational(1, 2)) == 0.5


def test_parse_from_string():
    assert Rational.from_string('3/4') == Rational(3, 4)


if __name__ == '__main__':
    test_operations()
    test_cast_to_float()
    test_parse_from_string()


# In[ ]:




