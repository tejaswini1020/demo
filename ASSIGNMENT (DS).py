#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[33]:


stud=[2305,'Teju','cse',89,'nellore'],[2056,'manu','cse',90,'kavali'],[2078,'Pavi','ece',95,'chithoor'],[2051,'kalai','ece',85,'chennai'],[2098,'riya','cse',92,'nagar'],[2045,'diya','eee',98,'nellore']
df=pd.DataFrame(stud,columns=['Rollno','Name','Dept','Marks','Location'])


# In[34]:


df


# In[35]:


df.head()


# In[36]:


df.tail()


# In[37]:


#rename
df.rename(columns={'Rollno':'Regno'})


# In[38]:


#delete
df.drop(columns=['Location'],inplace=True)


# In[39]:


df


# In[40]:


#display specific column
df['Rollno']


# In[41]:


#insert a new column
df.insert(4,"GPA",9.2)


# In[42]:


df


# In[43]:


#ascending order
df.sort_values("Marks")


# In[44]:


#null values
df.isnull()


# In[45]:


#sum of null values
df.isnull().sum()


# In[46]:


#sum of marks
df.Marks.sum()


# In[47]:


df.Marks.mean()


# In[48]:


df.Marks.max()


# In[49]:


df.Marks.min()


# In[51]:


#subset creation
df1=df[["Rollno","Name","Dept"]]


# 

# In[52]:


df1


# In[53]:


df['Marks'].plot()


# In[54]:


sns.lineplot(x='Name',y='Marks',data=df)


# In[55]:


sns.barplot(x='Name',y='Marks',data=df)


# In[ ]:




