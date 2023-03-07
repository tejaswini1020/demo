#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


ds=pd.read_csv('E:\president_heights.csv')


# In[3]:


ds


# In[4]:


#line graph
ds.plot()


# In[5]:


#bar chart
ds.plot.bar()


# In[6]:


ds.plot.bar(stacked=True)


# In[8]:


ds.plot.barh(stacked=True)


# In[9]:


ds.plot.box()


# In[10]:


ds.plot.area()


# In[11]:


ds.plot.scatter(x='order',y='height(cm)')


# In[ ]:




