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
