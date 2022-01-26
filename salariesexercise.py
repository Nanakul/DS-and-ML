import numpy as np
import pandas as pd

# Variables
salaries = pd.read_csv('Salaries.csv')

print(salaries)

# Check how many entries there are. == 148654
print(salaries.info())

# Calculate the average base pay. == 66325.45
salaries['BasePay'].replace({"Not Provided": np.nan}, inplace=True)
salaries['OvertimePay'].replace({"Not Provided": np.nan}, inplace=True)
salaries[['BasePay', 'OvertimePay']] = salaries[['BasePay', 'OvertimePay']].replace('', np.nan).astype(float)
print(salaries['BasePay'].mean())

# Highest amount of overtime pay? == 245131.88
print(salaries['OvertimePay'].max())

# Job title of JOSEPH DRISCOLL? == CAPTAIN, FIRE SUPPRESSION
print(salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL'])

