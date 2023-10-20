#!/usr/bin/env python
# coding: utf-8

# In[1]:


current_year=int(input("Enter current year:"))
final_year=int(input("Enter final year:"))
if(current_year%400==0 or(current_year%100 and current_year%4==0)):
    print("Current year is a leap year:",current_year)
print("The leap years are:")
for i in range(current_year,final_year):
    if(i%400==0 or(i%100 and i%4==0)):
        print(i)


# In[16]:


list1=[]
for i in range(0,5):
    n=int(input("Enter element:"))
    list1.append(n)
print("List elements are:",list1)
for i in list1:
    if(i<0):
        list1.remove(i)
print("List positive elements:",list1)


# In[24]:


list1=[]
for i in range(0,5):
    n=int(input("Enter element:"))
    list1.append(n)
print("List elements are:",list1)
list1=[i for i in list1 if i>0]
print(list1)


# In[18]:


list1=[]
for i in range(0,5):
    n=int(input("Enter a number:"))
    list1.append(n*n)
print("list items are:",list1)


# In[ ]:




