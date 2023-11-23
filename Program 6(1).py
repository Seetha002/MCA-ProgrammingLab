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


# In[28]:


def fibonacci(n):
    a=0
    b=1
    fib=0
    if n==0:
        return a
    elif n==1:
        return b
    else:
        print(a)
        print(b)
        for i in range(2,n):
            fib=a+b
            a=b
            b=fib
            print(fib)
num=int(input("Enter a number"))
print("The fibnoacci series for given number",num,"is:")
fibonacci(num)


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


# In[6]:


square=[]
initial=int(input("Enter initial number:"))
final=int(input("Enter final number:"))
for i in range(initial,final+1):
    sqr=i*i
    d=sqr
    while(d>0):
        digit=d%10
        if digit%2==0:
            d//=10
            if d==0:
                square.append(sqr)
        else:
            break
print(square)


# In[31]:


def pyramid(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print("\n")
n=int(input("Enter a number:"))
pyramid(n)


# In[11]:


string=input("Enter a string:")
length=len(string)
print("The length of given string is:",length)


# In[14]:


def modify(string):
    if string.endswith("ing"):
        newstring=string+"ly"
    else:
        newstring=string+"ing"
    return newstring
n=input("Enter a string:")
result=modify(n)
print(result)


# In[23]:


words=[]
def longest(word):
    lw=len(word[0])
    for i in word:
        current=len(i)
        if current>lw:
            lw=current
    print("the length of longest word is:",lw)
for i in range(0,4):
    n=input("Enter a word:")
    words.append(n)
longest(words)


# In[42]:


def pattern(row):
    for i in range(0,row):
        for j in range(0,i):
            print("*",end=" ")
        print("\n")
    for i in range(row,0):
        for j in range(i,0):
            print("*",end=" ")
        print("\n")
n=int(input("Enter a number:"))
pattern(n)


# In[ ]:




