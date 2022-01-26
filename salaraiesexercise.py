import numpy as np
import pandas as pd

# Variables
salaries = pd.read_csv('Salaries.csv')

print(salaries)

# Check how many entries there are. == 148654
print(salaries.info())

# Calculate the average base pay.
salaries['BasePay'].replace({"Not Provided": np.nan}, inplace=True)
salaries['OvertimePay'].replace({"Not Provided": np.nan}, inplace=True)
salaries[['BasePay', 'OvertimePay']] = salaries[['BasePay', 'OvertimePay']].replace('', np.nan).astype(float)
print(salaries['BasePay'].mean())

