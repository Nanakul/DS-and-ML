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

# How many people have the job title of Lawyer?
print(ecom[ecom['Job'] == 'Lawyer'].count())

# How many people made the purchase during the AM vs PM?
print(ecom['AM or PM'].value_counts())

# What are the 5 most common Job Titles?
print(ecom['Job'].value_counts().head(5))

# Someone made a purchase that came from Lot: '90 WT'
# What was the purchase price for this transaction?
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# What's the email of the person with the following credit card number?
# '4926535242672853'
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# How many people have Amex as their credit card and made a purchase above 95$?
print(ecom[(ecom['CC Provider'] == 'American Express') &
           (ecom['Purchase Price'] > 95)].count())

# How many people have a credit card that expires in 2025?
print(sum(ecom['CC Exp Date'].str.contains('/25')))

# What are the top 5 most popular email providers/hosts (gmail, yahoo, etc)?
print(ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5))
