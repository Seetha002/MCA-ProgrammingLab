# In[16]:


list1=[]
for i in range(0,5):
    n=int(input("Enter an integer:"))
    list1.append(n);
print(list1)
for i in list1:
    if(i%2==0):
        list1.remove(i)
print("After removing even numbers",list1)
