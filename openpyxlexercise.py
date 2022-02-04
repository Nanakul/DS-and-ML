from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# Create a new workbook
wb = Workbook()
ws = wb.active

# Create new worksheets
ws1 = wb.create_sheet('New Sheet')
ws2 = wb.create_sheet('First', 0)

# Alter title of current worksheet
ws.title = 'MySheet'

print(wb.sheetnames)

# Create a 2nd workbook and load an existing excel file.
wb2 = load_workbook('Regions.xlsx')
new_sheet = wb2.create_sheet('NewSheet')
active_sheet = wb2.active

# Access the value at cell A1
cell = active_sheet['A1']
print(cell.value)
