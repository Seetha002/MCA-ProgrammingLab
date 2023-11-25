# In[23]:


words=[]
def longest(word):
    lw=len(word[0])
    for i in word:
        current=len(i)
        if current>lw:
            lw=current
    print("the length of longest word is:",lw)
for i in range(0,4):
    n=input("Enter a word:")
    words.append(n)
longest(words)
