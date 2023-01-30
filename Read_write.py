# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:52:31 2023

@author: Sai khairnar
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users/HP/Documents/skilledge python programs/data/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users/HP/Documents/skilledge python programs/data/User_Data_1.csv')
print(df)
# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/HP/Documents/skilledge python programs/data/User_Data.xlsx')
print(df1)

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('C:/Users/HP/Documents/skilledge python programs/data/Sai_Khairnar.xlsx')
print(pandas.DataFrame(df1))