# In[28]:


import csv
file1=input("Enter file name:")
csvfile=open(file1,'r')
csvrow=csv.reader(csvfile)
col=int(input("Enter the column index:"))
for i in csvrow:
    if col<len(i):
        print(i[col])
csvfile.close()
