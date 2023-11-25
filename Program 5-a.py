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
