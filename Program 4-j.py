# In[18]:

dict1={}
dict2={}
for i in range(0,2):
    key1=int(input("Enter a key of dict1:"))
    value1=input("Enter value of dict1:")
    dict1[key1]=value1
for i in range(0,2):
    key2=int(input("Enter a key of dict2:"))
    value2=input("Enter value of dict2:")
    dict2[key2]=value2
print("The first Dictionary:",dict1)
print("The second Dictionary:",dict2)
dict1.update(dict2)
print("The merged dictionary:",dict1)
