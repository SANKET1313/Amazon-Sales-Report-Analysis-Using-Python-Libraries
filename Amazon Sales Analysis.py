#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv('Amazon Sale Report.csv',encoding= 'unicode_escape')


# df.head()

# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.drop(['New','PendingS'], axis=1, inplace=True)


# In[8]:


pd.isnull(df).sum()


# In[9]:


df.shape


# In[10]:


df.dropna(inplace=True)


# In[11]:


df.shape


# In[12]:


df.columns


# In[13]:


df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[14]:


df['ship-postal-code'].dtype


# In[17]:


df['Date']=pd.to_datetime(df['Date'])


# In[18]:


df.columns


# In[19]:


df.rename(columns={'Qty':'Quantity'})


# In[20]:


df.describe()


# In[21]:


df.describe(include='object')


# In[22]:


df[['Qty','Amount']].describe()


# # Exploratory Data Analysis

# In[23]:


df.columns


# size

# In[24]:


ax=sns.countplot(x='Size' ,data=df)


# In[25]:


ax=sns.countplot(x='Size' ,data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# Note: From above Graph you can see that most of the people buys M-Size
# Group By
# The groupby() function in pandas is used to group data based on one or more columns in a DataFrame

# In[26]:


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[29]:


S_Qty=df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

sns.barplot(x='Size',y='Qty', data=S_Qty)


# Note: From above Graph you can see that most of the Qty buys M-Size in the sales
# Courier Status

# In[30]:


sns.countplot(data=df, x='Courier Status',hue= 'Status')


# In[31]:


plt.figure(figsize=(10,5))

ax=sns.countplot(data=df, x='Courier Status',hue= 'Status')

plt.show()


# In[32]:


df['Size'].hist() 


# In[33]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=30, edgecolor='Black')
plt.xticks(rotation=90)
plt.show()


# In[34]:


B2B_Check = df['B2B'].value_counts()


plt.pie(B2B_Check, labels=B2B_Check, autopct='%1.1f%%')

plt.show()


# In[35]:


a1 = df['Fulfilment'].value_counts()

fig, ax = plt.subplots()

ax.pie(a1, labels=a1.index, autopct='%1.1f%%', radius=0.7, wedgeprops=dict(width=0.6))
ax.set(aspect="equal")

plt.show()


# In[36]:


x_data = df['Category']  
y_data = df['Size'] 


plt.scatter(x_data, y_data)
plt.xlabel('Category ')  
plt.ylabel('Size')  
plt.title('Scatter Plot') 
plt.show()


# In[39]:


plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[40]:


top_10_state = df['ship-state'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of  State')
plt.xticks(rotation=45)
plt.show()


# In[ ]:


Note: From above Graph you can see that most of the buyers are Maharashtra state
Conclusion
The data analysis reveals that the business has a significant customer base in Maharashtra state,
mainly serves retailers, fulfills orders through Amazon, experiences high demand for T-shirts, and
sees M-Size as the preferred choice among buyers.


# In[ ]:





# In[ ]:




