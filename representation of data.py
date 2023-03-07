#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


ds=pd.read_csv('E:\president_heights.csv')


# In[4]:


ds


# In[5]:


#to create a data frame
#data range is predefined in pandas
ds=pd.DataFrame(np.random.rand(10,4),index=pd.date_range('1/1/2000',periods=10),columns=list('ABCD'))


# In[7]:


ds.plot()


# In[9]:


sns.barplot(data=ds)


# In[12]:


ds.plot.bar()


# In[30]:


ds=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])


# In[31]:


ds.plot()


# In[32]:


ds.plot.bar()


# In[33]:


ds


# In[34]:


ds=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])


# In[36]:


ds.plot.bar(stacked=True)


# In[38]:


ds=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
ds.plot.barh(stacked=True)
#to display bar chart horizontally(barh)


# In[41]:


ds=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
ds.plot.box()


# In[45]:


ds=pd.DataFrame(np.random.rand(20,4),columns=['A','B','C','D'])
ds.plot.area()#area chart


# In[ ]:


ds=pd.DataFrame(np.random.rand(50,4),columns=['A','B','C','D'])
ds.plot.scatter(x='a')

