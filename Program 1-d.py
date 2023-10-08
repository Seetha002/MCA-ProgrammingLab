#!/usr/bin/env python
# coding: utf-8


list1=[]
for i in range(0,5):
    num=int(input("Enter an inetger:"))
    if(num>100):
        list1.append("over")
    else:
         list1.append(num)
print(list1)
