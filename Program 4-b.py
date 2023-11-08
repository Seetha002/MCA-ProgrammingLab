# In[15]:


string=input("Enter a string:")
newstring=string[0]+string[1:].replace(string[0],'$')
print("The new string is:",newstring)
