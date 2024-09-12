#!/usr/bin/env python
# coding: utf-8

# # FA FY 25 Salary Balance Tracking
# 
# Returning relevant expenditure accounts for FY 25 salary tracking.
# 
# - Current Month: **August**

# In[10]:


# importing packages
import tabula 
from tabula import read_pdf
import os
import pandas as pd
import string as str


# In[11]:


# setting JAVA_HOME and PATH variables
os.environ['JAVA_HOME'] = '/Users/scipio/Documents/FA_Budget_PDFs/jdk-22.0.2.jdk/Contents/Home'
os.environ['PATH'] = '/Users/scipio/Documents/FA_Budget_PDFs/jdk-22.0.2.jdk/Contents/Home/lib/server'


# In[12]:


# importing data
df1 = pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 1,
               pandas_options = {'header': None},multiple_tables = True)[0])
df2 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages =  2,
               pandas_options = {'header': None},multiple_tables = True)[0])
df3 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 3,
               pandas_options = {'header': None},multiple_tables = True)[0])
df4 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 4,
               pandas_options = {'header': None},multiple_tables = True)[0])
df5 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 5,
               pandas_options = {'header': None},multiple_tables = True)[0])
df6 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 6,
               pandas_options = {'header': None},multiple_tables = True)[0])
df7 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 7,
               pandas_options = {'header': None},multiple_tables = True)[0])
df8 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 8,
               pandas_options = {'header': None},multiple_tables = True)[0])
df9 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 9,
               pandas_options = {'header': None},multiple_tables = True)[0])
df10 =pd.DataFrame(tabula.read_pdf('/Users/scipio/Documents/FA_Budget_PDFs/All Accounts 08.31.24 Budget.PDF', pages = 10,
               pandas_options = {'header': None},multiple_tables = True)[0])

#combining tables
df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10])


# In[13]:


#creating. rename object
rename = {
    0:'Expend. Account #',
    1:'Account Title',
    2:'Original Bgt',
    3:'New App/Trnsf',
    4:'Revised Bgt',
    5:'Expenditures',
    6:'Encumbrances',
    7:'Avail Balance',
    8:'% Spent'}

df.rename(columns = rename, inplace = True) #--> renaming columns

df['Merge'] = df['Expend. Account #'].str.split(' ').str[0] #--> creating unique identifier
                 
# returning relevant columns
df = df[['Merge','Encumbrances','Avail Balance']]


# In[14]:


#creating dataframe
fy_25_salary_balance = pd.DataFrame(
    {'Account':['130-100-101-100-043','130-100-101-101-043','130-100-101-300-043',
                '130-100-101-301-043','140-100-101-500-043','140-100-101-501-043',
                '000-240-103-100-052','000-240-105-000-053','000-240-105-100-053',
                '000-262-110-000-066','000-240-105-300-053','000-219-104-000-066',
                '000-240-103-300-052','000-240-103-000-052','000-240-105-500-053',
                '000-240-103-500-052','250-100-100-000-097','231-100-100-000-096',
                '241-100-100-000-096']})

# merging dataframe to return relevent account data
fy_25_salary_df = fy_25_salary_balance.merge(df, left_on = 'Account',right_on = 'Merge', how = 'left')
fy_25_salary_df = fy_25_salary_df [['Account','Encumbrances','Avail Balance']]

#exporting data
fy_25_salary_df.to_csv('/Users/scipio/Documents/FA_Budget_PDFs/aug_salary_tracker.csv')

