# In[17]:


dict1={}
for i in range(0,4):
    key=int(input("Enter a key:"))
    value=input("Enter value:")
    dict1[key]=value
print("Dictionary in ascending order:",dict(sorted(dict1.items())))
print("Dictinoary in descending order:",dict(sorted(dict1.items(),reverse=True)))
