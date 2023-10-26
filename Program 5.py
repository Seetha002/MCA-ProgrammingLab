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


# In[15]:


string=input("Enter a string:")
newstring=string[0]+string[1:].replace(string[0],'$')
print("The new string is:",newstring)


# In[20]:


word=input("Enter a word:")
newword=word[-1]+word[1:-1]+word[0]
print(newword)


# In[ ]:





# In[ ]:




