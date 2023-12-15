# In[26]:


odd=[]
file1=input("Enter first file:")
file2=input("Enter second file:")
fileread=open(file1,'r')
filewrite=open(file2,'w')
lines=fileread.readlines()
for i in range(len(lines)):
    if i%2==0:
        odd.append(lines[i])
filewrite.writelines(odd)
filewrite.close()
print("Successfully copied odd lines from file1 to file2")
print(odd)
