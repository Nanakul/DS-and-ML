import numpy as np
import pandas as pd

ecom = pd.read_csv('ecommercepurchases.csv')
print(ecom.head())

# How many rows & columns are there? == 10k entries, 14 col
print(ecom.info())

# What is the Average Purchase Price? == 50.35
print(ecom['Purchase Price'].mean())

# What were the highest and lowest purchase prices?
# Highest == 99.99
print(ecom['Purchase Price'].max())
# Lowest == 0.0
print(ecom['Purchase Price'].min())

# How many people have 'en' as their language of choice on the website?
print(ecom[ecom['Language'] == 'en'].count())