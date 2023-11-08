#!/usr/bin/env python
# coding: utf-8

# In[11]:


fname=[]
coun=0
for i in range(0,5):
    ele=input("Enter your First Name:")
    fname.append(ele)
print(fname)
for i in fname:
    coun+=i.count('a')
print("The no. of occurance of a in the list is",coun)
