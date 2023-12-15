#!/usr/bin/env python
# coding: utf-8

# In[2]:


file=open('file1.txt','r')
lines=file.readlines()
file.close()
for i in lines:
    print(i)


# In[26]:


odd=[]
file1=input("Enter first file:")
file2=input("Enter second file:")
fileread=open(file1,'r')
filewrite=open(file2,'w')
lines=fileread.readlines()
for i in range(len(lines)):
    if i%2==0:
        odd.append(lines[i])
filewrite.writelines(odd)
filewrite.close()
print("Successfully copied odd lines from file1 to file2")
print(odd)


# In[28]:


import csv
file=input("Enter file name:")
csvfile=open(file,'r')
csvrow=csv.reader(csvfile)
print("Printing rows:")
for i in csvrow:
    print(i)
csvfile.close()


# In[29]:


import csv
file1=input("Enter file name:")
csvfile=open(file1,'r')
csvrow=csv.reader(csvfile)
col=int(input("Enter the column index:"))
for i in csvrow:
    if col<len(i):
        print(i[col])
csvfile.close()


# In[34]:


import csv
dict1={'Name':'sl','Age':21,'Course':'MCA'}
file1=input("Enter file name:")
csvfile=open(file1,'w',newline="")
csvwrite=csv.DictWriter(csvfile,fieldnames=dict1.keys())
csvwrite.writeheader()
csvwrite.writerow(dict1)
csvfile.close()
csvfile=open(file1,'r')
csvread=csv.reader(csvfile)
for i in csvread:
    print(i)
csvfile.close()


# In[ ]:





# In[ ]:




