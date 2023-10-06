#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("Enter an integer:"))
temp=str(n)
nn=temp+temp
nnn=temp+temp+temp
sum=n+int(nn)+int(nnn)
print("The value is: ",sum)


# In[22]:


list1=[]
for i in range(0,5):
    num=int(input("Enter an inetger:"))
    if(num>100):
        list1.append("over")
    else:
         list1.append(num)
print(list1)


# In[ ]:




