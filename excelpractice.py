import pandas as pd
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
