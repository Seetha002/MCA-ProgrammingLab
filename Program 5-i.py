#!/usr/bin/env python
# coding: utf-8




# In[42]:


def pattern(row):
    for i in range(0,row):
        for j in range(0,i):
            print("*",end=" ")
        print("\n")
    for i in range(row,0):
        for j in range(i,0):
            print("*",end=" ")
        print("\n")
n=int(input("Enter a number:"))
pattern(n)


# In[ ]:




