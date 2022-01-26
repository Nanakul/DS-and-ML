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

# How much does JOSEPH DRISCOLL make, including benefits? == 270324.91
print(salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

# What's the name of the highest paid person (including benefits)? == NATHANIEL FORD
print(salaries.sort_values(by='TotalPayBenefits', ascending=False))

# What's the name of the lowest paid person (including benefits)? == Joe Lopez
print(salaries.iloc[salaries['TotalPayBenefits'].argmin()])

# What was the average (mean) BasePay of all employees per year (2011-2014)?
print(salaries.groupby('Year').mean()['BasePay'])

# How many unique job titles are there? == 2159
print(salaries['JobTitle'].nunique())

# What are the top 5 most common jobs? == TO, SN, RN, Pub Aide, Police Office 3
print(salaries['JobTitle'].value_counts())

# 
