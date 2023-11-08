#!/usr/bin/env python
# coding: utf-8

# In[3]:


filename=input("Enter the filename:")
extension=filename.split('.')
print("The extension of given filename is:",extension[-1])



# In[15]:


colors=input("Enter a list of colors with comma:")
newcolors=colors.split(',')
print("The first color is:",newcolors[0])
print("The last color is:",newcolors[-1])


# In[26]:


color_list1=input("Enter first list of colors:")
color_list1=color_list1.split(',')
color_list2=input("Enter second list of colors:")
color_list2=color_list2.split(',')
print("first list of colors:",color_list1)
print("Second list of colors:",color_list2)
diff=set(color_list1) - set(color_list2)
print("colors present in list1 and not in list2 is:",diff)


# In[5]:


string1=input("Enter a string1:")
string2=input("Enter a string2:")
string3=string2[0]+string1[1:]+" "+string1[0]+string2[1:]
print("New string is:",string3)


# In[14]:


n=input("Enter a string:")
w=n.split(" ")
new=[]
print("The string is:",w)
for i in w:
    if i not in new:
        new.append(i)
print(new)
for i in new:
    count=0
    for j in w:
        if i==j:
            count=count+1
    print("The string ",i,"has ",count," times words")


# In[17]:


dict1={}
for i in range(0,4):
    key=int(input("Enter a key:"))
    value=input("Enter value:")
    dict1[key]=value
print("Dictionary in ascending order:",dict(sorted(dict1.items())))
print("Dictinoary in descending order:",dict(sorted(dict1.items(),reverse=True)))


# In[18]:


dict1={}
dict2={}
for i in range(0,4):
    key1=int(input("Enter a key of dict1:"))
    value1=input("Enter value of dict1:")
    dict1[key1]=value1
    key2=int(input("Enter a key of dict2:"))
    value2=input("Enter value of dict2:")
    dict1[key2]=value2
dict1=dict1.update(dict2)


# In[ ]:




