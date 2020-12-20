#!/usr/bin/env python
# coding: utf-8

# 
# ## LabDS01 ##
# 
# 
# The following dataset includes information about several countries. This information was collected by the world bank (https://data.worldbank.org/). Data corresponds to 2016.
# 
# `
# dataFile="https://raw.githubusercontent.com/masterfloss/data/main/worlddata2016.xlsx"
# df=pd.read_excel(dataFile)
# `
# 

# # 1. Business Understanding
# 
# Purpose: Analyse data and extract knowledge
# 
# Observation: Country
# 

# In[7]:



import pandas as pd
dataFile="https://raw.githubusercontent.com/masterfloss/data/main/worlddata2016.xlsx"
df=pd.read_excel (dataFile)

df1= pd.pivot_table(df, values='2016', index=['Country Name'], columns=['Indicator Name'])
df1


# In[9]:


df.dtypes


# # 2. Data Undertanding
# 
# * Discuss the data and purposes
# * What are the main limitations?

# In[8]:


pos1=pd.get_dummies(df['Indicator Name'], prefix='ID')
pos1


# # 3. Data Preparation
# 
# * Converting data to numeric
# * Missing Values Imputation
# * Normalization
# * Variable Dummification
# * Data balancing
# * Pivot date in order to convert the values "Indicator Name" into comuns 
# * Remove all columns that have no values, df1[columns].sum()==0
# * Remove all columns that have more than 210 observations, df1[columns].count()<210

# In[ ]:




