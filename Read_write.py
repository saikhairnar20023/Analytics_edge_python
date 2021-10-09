# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:10:42 2021

@author: ABC
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users/ABC/Documents/Business_analytics_python/User_Data_1.csv')
print(df)
# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/ABC/Documents/Business_analytics_python/DATA/User_Data.xlsx')
print(df1)

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('C:/Users/ABC/Documents/Business_analytics_python/Sai_Khairnar.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)