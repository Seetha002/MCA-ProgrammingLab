# In[28]:


import csv
file=input("Enter file name:")
csvfile=open(file,'r')
csvrow=csv.reader(csvfile)
print("Printing rows:")
for i in csvrow:
    print(i)
csvfile.close()
