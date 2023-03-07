#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


ds=pd.read_csv('E:\president_heights.csv')


# In[4]:


ds


# In[5]:


import seaborn as sns


# In[7]:


sns.barplot(x='name',y='height(cm)',data=ds)


# In[9]:


plt.figure(figsize=(15,5))


# In[11]:


sns.barplot(x='name',y='height(cm)',data=ds)
plt.xticks(rotation=90)
plt.figure(figsize=(100,50))


# In[12]:


sns.barplot(x='name',y='height(cm)',data=ds)
plt.ylim(100,200)
plt.xticks(rotation=90)
plt.figure(figsize=(100,50))


# In[13]:


sns.barplot(x='name',y='height(cm)',data=ds)
plt.title("Presidents Height")
plt.ylim(100,200)
plt.xticks(rotation=90)
plt.figure(figsize=(100,50))


# In[18]:


sns.barplot(x='order',y='height(cm)',data=ds,color='Lightgreen')#colour for the graph
plt.title("Presidents order")
plt.ylim(100,200)#extending the y limit
plt.xticks(rotation=90)#to rotate the numbers or alphabets on x axis
plt.figure(figsize=(100,50))#to show the picture size


# In[19]:


sns.barplot(x='name',y='height(cm)',data=ds,color="Lightgreen")
plt.title("Presidents Height")
plt.ylim(170,180)
plt.xticks(rotation=90)
plt.figure(figsize=(100,50))


# In[25]:


#to create a pandas series
data=pd.Series([1.0,1.5,1.75,2.0],index=['a','b','c','d'])

when we create a dataset index value we need to mention the values to index values
# In[26]:


data


# In[27]:


#to display b index
data['b']


# In[29]:


#to check whether a is present in the data series
'a' in data


# In[30]:


'f' in data


# In[32]:


#to display key values(insex values)
data.keys()


# In[33]:


#to make a list from the created dataset
list(data.items())


# In[35]:


#to insert the value
data['e']=2.5


# In[36]:


data


# In[39]:


#to print c,d,e values
data[2:7]


# In[40]:


data['c':'e']


# In[41]:


data[1:3]


# In[42]:


data


# In[48]:


#to display the range 
data[(data>1.5)&(data<2.5)]


# In[49]:


data


# In[50]:


data[1]


# In[51]:


data[1:3]


# In[52]:


area=({'Chennai':91,'Nellore':92,'Kerela':93,'Mumbai':94,'Delhi':96})


# In[53]:


area


# In[54]:


area.keys()


# In[55]:



pop=area=pd.Series({'Chennai':91,'Nellore':92,'Kerela':93,'Mumbai':94,'Delhi':96})


# In[56]:


pop


# In[57]:


area


# In[59]:


#panda series into dataset
data=pd.DataFrame({'area':area,'pop':pop})


# In[60]:


data


# In[71]:


data['density']=data['pop']+data['area']


# In[73]:


data


# In[74]:


data


# In[75]:


data=pd.DataFrame({'area':area,'pop':pop})


# In[76]:


data


# In[77]:


#to insert a new column
data['density']=data['pop']+data['area']


# In[78]:


data


# In[82]:


data.values


# In[86]:


data.values[2]


# In[87]:


data.values[:1]


# In[88]:


ds


# In[89]:


ds.iloc[4]


# In[90]:


data


# In[91]:


data.iloc[0]


# In[92]:


#to display density value
data.iloc[0,2]


# In[93]:


#to change the density value
data.iloc[0,2]=160


# In[94]:


data


# In[95]:


data


# In[98]:


data[(data.density>180)]


# In[99]:


#to create a series with null values
data1=pd.Series([1,np.nan,2,None,3],index=['a','b','c','d','e'])


# In[100]:


data1


# In[101]:


#to fill the null values
data1.fillna(0)


# In[102]:


#displays previous value/forward va;ue
data1.fillna(method='ffill')


# In[103]:


data1.fillna(method='bfill')


# In[ ]:




