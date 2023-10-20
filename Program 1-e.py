# In[14]:


def gcd1(a,b):
    if(b==0):
        return a
    else:
        return gcd1(b,a%b)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
g=gcd1(num1,num2)
print("gcd of num1 and num2 is:",g)
