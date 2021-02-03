#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Question: Create a list and swap the second half of the list with the first half of the list and print this list on the screen

List=[1,2,3,4,5,6,7,8,9,10]

Length=len(List)

half=int(Length/2)

Firsthalf=List[:half]
Secondhalf=List[half:]

Swapped_List=[Secondhalf+Firsthalf]
print(Swapped_List)

[[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]]


# In[ ]:




