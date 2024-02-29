#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importing Libraries

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns


# In[9]:


#importing the data set

data=pd.read_csv(r"C:\Users\spoorthiv.vc\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv",encoding="unicode_escape")
data


# In[11]:


#checking the shape

data.shape


# In[12]:


#to check the view of data columns this gives first 5 rows and all columns

data.head()


# In[14]:


#to know the data information which is helpful to clean the data
data.info()


# In[27]:


# as per inform satus and unnamed1 doesnot have any data deleting the columns
#axis=1 it considers the complete row
#inplace=True considers to save the action done

data.drop(['Status','unnamed1'],axis=1,inplace=True)
print(data.columns)


# In[28]:


#checkng the drop operations 

print(data.columns)


# In[30]:


#checking null values by suming the count of nullvalue in column

pd.isnull(data).sum()


# In[31]:


#checking the shape for reference

data.shape


# In[32]:


#deleting null values

data.dropna(inplace=True)


# In[33]:


#checking shape after operation

data.shape


# In[35]:


pd.isnull(data).sum()


# In[45]:


#changing data type of amount column as its float

data['Amount']=data['Amount'].astype('int')


# In[46]:


#checking the changes

data['Amount'].dtypes


# In[47]:


#printing colums 

data.columns


# In[48]:


#renaming the columns

data.rename(columns={'Marital_Status':'Shaadi'})


# In[49]:


#getting the discription of the data

data.describe()


# In[51]:


#to check the description for particular columns

data[['Amount','Orders']].describe()


# In[52]:


#Exporatory Data Analysis(EDA)


# In[54]:


data.columns


# In[58]:


ax=sns.countplot(x='Gender',data=data)


# In[59]:


ax=sns.countplot(x='Gender',data=data)
for bars in ax.containers:
    ax.bar_label(bars)


# In[70]:


#grouping by gender and suming purchase value

group=data.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
group


# In[72]:


group=data.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
gra=sns.barplot(x='Gender',y='Amount',data=group)
for bars in gra.containers:
    gra.bar_label(bars)


# In[74]:


#from the above graph we can see that most of the buyers are female with max purchase power


# In[78]:


#Age basis analysis

age_group=sns.countplot(data=data,x='Age Group',hue='Gender')


# In[79]:


age_group=sns.countplot(data=data,x='Age Group',hue='Gender')
for bars in age_group.containers:
    age_group.bar_label(bars)


# In[81]:


#age group expenditure analysis

age_sum=data.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
age_sum


# In[90]:


age_sum=data.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
gra=sns.countplot(data=data,x='Age Group',hue='Gender')
for bars in gra.containers:
    gra.bar_label(bars)


# In[91]:


#from the above plot we can summarise female between 26-35 


# In[94]:


#state

stat=data.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
stat


# In[114]:


stat=data.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
gra1=sns.countplot(data=data,x='State')
gra1


# In[116]:


#Orders

ord=data.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by=['State'],ascending=False).head(5)
ord


# In[183]:





# In[187]:


dh=data.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by=['State'],ascending=False).head(5)
sns.barplot(data=data,x='Orders',y='State')
for bars in dh.containers:
    dh.bar_label(bars)


# In[184]:


dh


# In[145]:


#marital status

mar=sns.countplot(data=data,x="Marital_Status")
sns.set(rc={'figure.figsize':(2,1)})
mar
for bars in mar.containers:
    mar.bar_label(bars)


# In[185]:


mar


# In[137]:


data.columns


# In[147]:


data.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by=['Amount'],ascending=False).head(5)


# In[161]:


b=data.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(10,2)})
gh=sns.barplot(data=b,x='Marital_Status',y='Amount',hue='Gender')


# In[168]:


#occupation 

a=data.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data=a,x='Occupation',y='Amount')


# In[169]:


#product category 

sns.set(rc={'figure.figsize':(20,5)})
h=sns.countplot(data=data,x='Product_Category')
for bars in h.containers:
    h.bar_label(bars)
   


# In[177]:


prod=data.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by=['Amount'],ascending=False).head()
prod
sns.barplot(data=prod,x='Amount',y='Product_Category')
for bars in prod.containers:
    prod.bar_label(bars)


# In[178]:


#product category 

j=data.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data=j,x='Product_ID',y='Orders')


# In[ ]:


#women maaried age group 26-35 belongd UP,Maharastra belongs to IT industry and has brought Food and Clothing

