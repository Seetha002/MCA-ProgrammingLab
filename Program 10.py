#!/usr/bin/env python
# coding: utf-8

# In[2]:


file=open('file1.txt','r')
lines=file.readlines()
file.close()
for i in lines:
    print(i)

