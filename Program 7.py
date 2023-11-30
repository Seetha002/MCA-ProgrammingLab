#!/usr/bin/env python
# coding: utf-8

# In[3]:


sqarea=lambda s:s*s
rectarea=lambda l,b:l*b
triarea=lambda h,ba:(1/2)*h*ba


s=int(input("Enter the side length of square:"))
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
h=int(input("Enter height of Triangle:"))
ba=int(input("Enter base of Triagnle:"))

print("Area of square:",sqarea(s))
print("Area of Rectangle:",rectarea(l,b))
print("Area of Triangle:",triarea(h,ba))


# In[ ]:




