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


# In[27]:


vowels=['a','e','i','o','u','A','E','I','O','U']
vow=[]
word=input("Enter an word:")
vow=[i for i in word if i in vowels]
print(vow)


# In[28]:


word=input("Enter a word:")
ordinal_value=[ord(i) for i in word]
print("Ordinal values are:",ordinal_value)


# In[ ]:




