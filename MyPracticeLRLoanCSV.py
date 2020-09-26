#!/usr/bin/env python
# coding: utf-8

# # Linear regression Practice at home

# In[1]:


import pandas as pd


# Load the Input Data file 

# In[2]:


df=pd.read_csv("C:/Users/satkari/Desktop/New folder/ATT-UV/Python_practice/loans data.csv")


# In[3]:


df.isnull()


# Display DF

# In[3]:


df


# with the help pf Dataframe info check the datatype of each column again and its noticed that whichever all columns we see as object we need to conver them to float as linear regression takes all the inputs as numeric

# In[4]:


df.info()


# In[5]:


df["Amount.Requested"]=pd.to_numeric(df["Amount.Requested"],errors="coerce")


# to_numeric is used to conver Amount requested column values to numeric from float and in case if any of the value cant be converted to number will be convereted to NAN becasue we gave errors as coerse parameter

# In[6]:


df.info()


# In[7]:


df


# Now since Interest column is with percentage we need to replace % suffix from the column so is the below line 

# In[8]:


df["Interest.Rate"]=df["Interest.Rate"].str.replace("%","")


# In[9]:


df


# In[10]:


df.info()


# Checking with info if the Interest rate has been changed to Float but since its still not changed to float we need to change it to numeric with to_numeric function of pandas 

# In[11]:


df["Interest.Rate"]=pd.to_numeric(df["Interest.Rate"],errors="coerce")


# In[12]:


df.info()# now Interst rate has been changed to float so we are good 


# In[13]:


df


# Since loan Lenght is also of type object and it has text "months" suffixed so we need to remove it so is below code line 

# In[14]:


df["Loan.Length"]=df["Loan.Length"].str.replace("months","")


# In[15]:


df


# In[16]:


df.info()


# Since loan lenght column still apear to be object we need to convert it to float so is the below code line 

# In[17]:


df["Loan.Length"]=pd.to_numeric(df["Loan.Length"],errors="coerce")


# In[18]:


df


# In[19]:


df.info()


# Similarly we will remove "%" sign from Debt_To_income_ratio Column as well

# In[20]:


df["Debt.To.Income.Ratio"]=df["Debt.To.Income.Ratio"].str.replace("%","")


# In[21]:


df


# In[22]:


df.info()


# In[23]:


df["Debt.To.Income.Ratio"]=pd.to_numeric(df["Debt.To.Income.Ratio"],errors="coerce")


# In[24]:


df.info()


# In[25]:


df["Open.CREDIT.Lines"]=pd.to_numeric(df["Open.CREDIT.Lines"],errors="coerce")


# In[26]:


df.info()


# In[27]:


df["Revolving.CREDIT.Balance"]=pd.to_numeric(df["Revolving.CREDIT.Balance"],errors="coerce")


# In[28]:


df.info()


# In[29]:


df["Home.Ownership"].value_counts()


# In[30]:


dummy=pd.get_dummies(df["Home.Ownership"])


# In[31]:


dummy.head()


# In[32]:


df=pd.concat([df,dummy],axis=1)


# In[33]:


df


# In[34]:


df=df.drop(["Home.Ownership"],axis=1)


# In[35]:


df


# In[36]:


df.isnull().sum()


# In[37]:


df=df.dropna()


# In[38]:


df.isnull().sum()


# In[39]:


import matplotlib.pyplot as plt
import statsmodels.api as sm


# In[40]:


fig=sm.qqplot(df["Interest.Rate"])


# In[41]:


import seaborn as sns
sns.distplot(df["Amount.Requested"])
plt.show()


# In[42]:


df.info()


# In[43]:


df.isna().sum()


# In[44]:


df.dropna()


# In[45]:


df.info()


# In[ ]:


correlation_matrix=df.corr().round(2)
sns.heatmap(data=correlation_matrix,annot=True)
plt.show()
plt.figure(figsize=(800,500))


# In[ ]:




