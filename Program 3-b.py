#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[]
square=[]
for i in range(0,5):
    n=int(input("Enter an number:"))
    list1.append(n)
square=[i*i for i in list1]    
print("Square list of given list is:",square)
