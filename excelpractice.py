import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

# Load/Save data with pandas
df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_text = pd.read_csv('data.txt', delimiter='\t')

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Zip', 'Salary']
df_csv.to_excel('modified.xlsx')

# View and inspect data with pandas
print(df_csv[['State', 'Zip']])
print(df_csv['First'][0:3])
print(df_csv.iloc[1])

wanted_values = df_csv[['First', 'Last', 'Salary']]
stored = wanted_values.to_excel('person_salary.xlsx', index=None)

# Organize, Sort, and Filter data with Pandas

# Find People that live in Riverside
print(df_csv.loc[df_csv['City'] == 'Riverside'])
# Find all people that live in Riverside AND that have the name John
print(df_csv.loc[(df_csv['City'] == 'Riverside') & (df_csv['First'] == 'John')])

# Create a 'Tax %' column
df_csv['Tax %'] = df_csv['Salary'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)
print(df_csv)

# Create a 'Taxes Owed' column
df_csv['Taxes Owed'] = df_csv['Salary'] * df_csv['Tax %']

# Create a 'Sal After Tax' column
df_csv['Sal After Tax'] = df_csv['Salary'] - df_csv['Taxes Owed']
print(df_csv)

# Drop columns
to_drop = ['Zip', 'First', 'Address']
df_csv.drop(columns=to_drop, inplace=True)
print(df_csv)

# Create Conditional Check Column of Bools
df_csv['Conditional'] = False

# Change Conditional column to True IF Salary < 60000
df_csv.loc[df_csv['Salary'] < 60000, 'Conditional'] = True
print(df_csv)

# Groupby Conditional column and also calculate the mean.
print(df_csv.groupby(['Conditional']).mean())

# Sort data by Salary
print(df_csv.groupby(['Conditional']).mean().sort_values('Salary'))

# Cleaning data
df_csv = df_csv.set_index('City')
print(df_csv.loc['Riverside'])

# Read everyone's first name and use a string function to split by spaces.
df_csv.Last = df_csv.Last.str.split(expand=True)
print(df_csv)

# If there is a NaN value, you can replace it with the following line:
# df_csv = df_csv.replace(np.nan, 'N/A', regex=True)

to_excel = df_csv.to_excel('modified.xlsx')
