#!/usr/bin/env python
# coding: utf-8

# In[5]:


list1 = ["a", "b", "c", "d"]
index1 = list1.index("a")
index2 = list1. index("c")
index3 = list1.index("b")
index4 = list1. index("d")
list1[index1], list1[index2] = list1[index2], list1[index1]
list1[index3], list1[index4] = list1[index4], list1[index3]
print(list1)


# In[14]:


n = int(input("Enter a number: "))
for i in range(n+1):
    if (i % 2) == 0:
       print("{} is Even".format(i))
    else:
       print("{} is Odd".format(i))


# In[ ]:




