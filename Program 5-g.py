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
