#!/usr/bin/env python
# coding: utf-8

# In[26]:


def factorial(n):
    fact=1
    if n<0:
        print("invaild input")
        return
    elif n==0:
        return 0
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact
num=int(input("Enter a number to find Factorial:"))
result=factorial(num)
print("The factorial of given number:",result)


# In[34]:


list1=[]
total=0
for i in range(4):
    n=int(input("Enter a number"))
    list1.append(n)
print(list1)    
for i in list1:
    total=total+i
print("Sum of all items in the list:",total)


# In[53]:


square=[]
initial=int(input("Enter initial number:"))
final=int(input("Enter final number:"))
for i in range(initial,final+1):
    sqr=i*i
    d=sqr
    while(d>=0):
        digit=d%10
        if digit%2!=0:
            break
        d/=10
    if d==0:
        square.append(sqr)
print(square)


# In[ ]:




