import pandas as pd 
import numpy as np 

df = pd.read_csv("./data/ecommerce_customers.csv")

print(df.head)

print(df.info())

print(df.isnull().sum())

print(df.duplicated().sum())

# Drop unnessesary columns

columns_to_drop = ['Email', 'Address', 'Avatar']
df_cleaned = df.drop(columns_to_drop, axis = 1)

df_cleaned.to_csv('ecommerce_customers_cleaned.csv', index=False)