#!/usr/bin/env python
# coding: utf-8

# In[13]:


list1=[4,5,6,7]
list2=[1,2,3,4]
print("list1:",list1)
print("list2:",list2)
x=len(list1)
y=len(list2)
if(x==y):
    print("These two list has same length")
else:
    print("Not of same length")
a=sum(list1)
b=sum(list2)
if(a==b):
    print("two list have same sum values")
else:
    print("Does not have same sum values")
count=0
for i in list1:
    for j in list2:
        if(i==j):
            count=count+1
            print("Two list have same value:",i)
if(count==0):
    print("No same value are there")
