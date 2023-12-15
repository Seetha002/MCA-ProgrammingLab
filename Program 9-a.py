#!/usr/bin/env python
# coding: utf-8

# In[2]:


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if self.area()==other.area():
            print("Two rectangles have same area")
        else:
            print("Does not have same area")
rect1=rectangle(5,10)
rect2=rectangle(8,6)
print("Area of rectangle 1 is:",rect1.area())
print("Perimeter of rectangle 1 is:",rect1.perimeter())
print("Area of rectangle 2 is:",rect2.area())
print("Perimeter of rectangle 2 is:",rect2.perimeter())
rect1.compare(rect2)
