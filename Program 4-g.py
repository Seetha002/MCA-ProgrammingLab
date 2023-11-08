# In[26]:


color_list1=input("Enter first list of colors:")
color_list1=color_list1.split(',')
color_list2=input("Enter second list of colors:")
color_list2=color_list2.split(',')
print("first list of colors:",color_list1)
print("Second list of colors:",color_list2)
diff=set(color_list1) - set(color_list2)
print("colors present in list1 and not in list2 is:",diff)
