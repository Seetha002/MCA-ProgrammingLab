# In[6]:


square=[]
initial=int(input("Enter initial number:"))
final=int(input("Enter final number:"))
for i in range(initial,final+1):
    sqr=i*i
    d=sqr
    while(d>0):
        digit=d%10
        if digit%2==0:
            d//=10
            if d==0:
                square.append(sqr)
        else:
            break
print(square)
