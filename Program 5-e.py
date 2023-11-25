# In[31]:


def pyramid(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print("\n")
n=int(input("Enter a number:"))
pyramid(n)
