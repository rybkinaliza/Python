#!/usr/bin/env python
# coding: utf-8

# In[44]:


import math

class Point:
    def __init__(self, r, phi):
        self.r = r
        self.phi = phi
        
    def __add__(self, other):
        if self.phi > other.phi:
            phi_max = self.phi
            r_max = self.r
            phi_min = other.phi
            r_min = other.r
        else :
            phi_max = other.phi
            r_max = other.r
            phi_min = self.phi
            r_min = self.r
        delta_phi = phi_max - phi_min
        r_result = round(math.sqrt(r_min**2 + r_max**2 - 2*r_min*r_max*math.cos(math.radians(delta_phi))), 2)
        phi_result = round(math.degrees(math.acos((r_min**2 + r_result**2 - r_max**2)/(2*r_min*r_result))) + phi_min)
        return Point(r_result, phi_result)
    
    def __str__(self):
        return f'r={self.r}, phi={self.phi}'
    
    def __repr__(self):
        return f'Point({self.r}, {self.phi})'
    
    def from_cartesian(x, y):
        r = round(math.sqrt(x**2 + y**2), 2)
        if x>0 and y>=0:
            phi = round(math.degrees(math.atan(y/x)))
        if x<0 and y>=0:
            phi = 90 + round(abs(math.degrees(math.atan(y/x))))
        if x<0 and y<=0:
            phi = 180 + round(abs(math.degrees(math.atan(y/x))))
        if x>0 and y<0:
            phi = 270 + round(abs(math.degrees(math.atan(y/x))))
        return Point(r, phi)
    
    def __eq__(self, other):
        if self.r == other.r and abs(self.phi - other.phi) % 360 == 0:
            return True
        else:
            return False


# In[ ]:





# In[ ]:




