import numpy as np
import pandas as pd

ecom = pd.read_csv('ecommercepurchases.csv')
print(ecom.head())

# How many rows & columns are there? == 10k entries, 14 col
print(ecom.info())

# What is the Average Purchase Price? == 50.35
print(ecom['Purchase Price'].mean())
