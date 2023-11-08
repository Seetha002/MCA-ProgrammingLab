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

