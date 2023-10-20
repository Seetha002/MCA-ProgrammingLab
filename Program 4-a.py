
# In[24]:


list1=[]
for i in range(0,5):
    n=int(input("Enter element:"))
    list1.append(n)
print("List elements are:",list1)
list1=[i for i in list1 if i>0]
print(list1)

