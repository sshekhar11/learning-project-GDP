#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("GDP_Sector_Income_2019_2023_30Cities.csv")
print(df.head(100))


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.tail()


# In[7]:


df.head(100)


# In[8]:


pd.isnull(df).sum()


# In[9]:


pd.isnull(df)


# In[10]:


#drop null values
df.dropna


# In[11]:


df.shape


# In[12]:


df.columns


# In[13]:


df.info()


# In[14]:


#changing data type
df['GDP (in billion $)']=df['GDP (in billion $)'].astype('int')


# In[15]:


df['GDP (in billion $)'].dtype


# In[17]:


#for specific column
df[['City','Year']].describe()


# # Exploratory data analysis

# In[18]:


df.columns


# # Size

# In[22]:


ax=sns.countplot(x='Year', data=df)


# In[23]:


ax=sns.countplot(x='Year', data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# # Group by
# the groupby() function in pandas is used to group data based on one or more columns in Daraframe.

# In[24]:


df.groupby(['Year'], as_index= False)['City'].sum().sort_values(by= 'City', ascending=False)


# In[26]:


Ss=df.groupby(['Year'], as_index= False)['City'].sum().sort_values(by= 'City', ascending=False)
sns.barplot(x='City' , y='Year', data=Ss)


# In[27]:


plt.figure(figsize=(10,5))
ax=sns.countplot(data=df, x='Agriculture (%)' ,hue= 'Year')
plt.show()


# In[28]:


#histogram 
df['Year'].hist()


# In[ ]:


#plt.pie()
#plt.scatter

