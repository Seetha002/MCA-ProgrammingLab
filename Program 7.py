#!/usr/bin/env python
# coding: utf-8

# In[4]:


factors=[]
n=int(input("Enter a number:"))
for i in range(1,n):
    if n%i==0:
        factors.append(i)
print("The factors of ",n," is ",factors)


# In[ ]:




