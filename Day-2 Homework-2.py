#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Question: Ask the user to enter a single digit integer to a variable 'n'. Then print out all of the even numbers from 0 to n 

n=int(input("Enter a single digit integer"))
for num in range (n):
    if num%2==0:
        print (num)
        

***
Answer:
Enter a single digit integer9
0
2
4
6
8
***

