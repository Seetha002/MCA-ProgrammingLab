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
