#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np


# In[71]:


df=pd.read_csv('homeprices_2.csv')
df.head()


# In[72]:


df.isnull().sum()


# In[73]:


plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['area'],df['price'],marker='o',color='red')
plt.title('Area VS Price')


# In[74]:


plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['age'],df['price'],marker='o',color='red')
plt.title('Age VS Price')


# In[75]:


plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['bedrooms'],df['price'],marker='o',color='red')
plt.title(' Bedrooms VS Price')


# In[76]:


#independent variables
x=df[['area','age','bedrooms']]
x


# In[77]:


#dependent variable
y=df.price
y


# In[78]:


model=linear_model.LinearRegression()


# In[79]:


model.fit(x,y) # it will fit the data and find intercept and coefficient


# In[80]:


model.coef_


# In[81]:


model.intercept_


# In[82]:


area=int(input("Enter the area"))
bedroom=int(input("Enter the bedrooms:"))
age=int(input("Enter the age:"))
result=model.predict([[area,bedroom,age]])
print(f'The prediction is:${result}')


# In[ ]:




