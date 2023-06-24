#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


connection=sqlite3.connect("sample.db")


# In[4]:


table="CREATE TABLE people(id integer primary key, name TEXT, surname TEXT) " #we are creating a query called table


# In[10]:


cursor=connection.cursor() #creating a cursor


# In[11]:


cursor.execute (table)


# In[13]:


connection.commit() #these codes create a file called sample.db


# In[ ]:




