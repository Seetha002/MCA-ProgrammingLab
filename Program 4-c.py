# In[27]:


vowels=['a','e','i','o','u','A','E','I','O','U']
vow=[]
word=input("Enter an word:")
vow=[i for i in word if i in vowels]
print(vow)
