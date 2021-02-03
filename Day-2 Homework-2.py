#!/usr/bin/env python
# coding: utf-8

# In[11]:


"""Question: Ask the user to enter a single digit integer to a variable 'n'. Then print out all of the even numbers from 0 to n 
including n"""

n=int(input("Enter a single digit integer"))

for num in range (n+1):
    if num%2==0:
        print (num)
        
        


        

