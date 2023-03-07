#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


ds=pd.read_csv('E:\president_heights.csv')


# In[6]:


ds


# In[9]:


ds.rename(columns={'height(cm)':'height'})


# In[10]:


ds


# In[11]:


#to permanentaly change the column a name
ds.rename(columns={'height(cm)':'height'},inplace=True)


# In[12]:


ds


# In[13]:


ds


# In[15]:


#to insert a new column and assign the values for the column
ds.insert(3,"age","50")


# In[16]:


ds


# In[18]:


ds.insert(2,"quality","Good")


# In[19]:


ds


# In[25]:


#to remove particular column from the dataset
ds.drop(columns=['quality'])


# In[29]:


ds.drop(columns=['age'] ,inplace=True)


# In[30]:


ds


# In[32]:


#to display the height values
ds['height']<175


# In[34]:


3to display 
ds[ds['height']<=175]


# In[36]:


ds[((ds['height']>=175)&(ds['height']<180))]


# In[37]:


#to find out the null value
#if there is null value it display true
ds.isnull()


# In[38]:


ds


# In[42]:


#sum of heights
sum(ds['height'])


# In[44]:


#visualization packet tool
import seaborn as sns


# In[45]:


#to display barchart
mark=[90,80,88,95,92,90]
subject=['Telugu','English','Hindi','Science','Social','Maths']
plt.bar(subject,mark)


# In[53]:


mark=[90,89,88,95,92,90]
subject=['Telugu','English','Hindi','Science','Social','Maths']
plt.bar(subject,mark)
plt.title("Student marks")
plt.xlabel('marks')
plt.ylabel('subject')
#to extend the limit of barchart
plt.ylim(50,200)
plt.show()


# In[54]:


#barchart for the dataset columns
sns.barplot(x='name',y='height',data=ds)


# In[ ]:




