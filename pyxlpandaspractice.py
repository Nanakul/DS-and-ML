import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font

df_1 = pd.read_excel('shifts.xlsx', sheet_name='Sheet')
df_2 = pd.read_excel('shifts.xlsx', sheet_name='Sheet1')
df_3 = pd.read_excel('shift_3.xlsx')

# Concatenate to combine all of the data frames
df_all = pd.concat([df_1, df_2, df_3], sort=False)

print(df_all)

to_excel = df_all.to_excel('all_shifts.xlsx', index=None)

wb = load_workbook('all_shifts.xlsx')
ws = wb.active

# Create new column called 'Total' with bold font in column G
total_col = ws['G1']
total_col.font = Font(bold=True)
total_col.value = 'Total'

