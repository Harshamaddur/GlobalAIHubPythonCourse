#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Question: User Login Application
# Get user name and password values from the user 
# check the values in an if statement and tell the user if they were successful

User_name="Harsha"
Password="12345"

User_name1=input("Enter the user name")
Password1=input("Enter the Password")

if User_name1==User_name and Password1!=Password:
    print ("Invalid Password")
elif User_name1!=User_name and Password1==Password:
    print("Invalid User name")
elif User_name1!=User_name and Password1!=Password:
    print("Both user name and password are incorrect")
else:
    print("Login Successful")


# In[ ]:




