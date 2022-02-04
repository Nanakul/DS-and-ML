import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_text = pd.read_csv('data.txt', delimiter='\t')

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Zip', 'Salary']
df_csv.to_excel('modified.xlsx')
