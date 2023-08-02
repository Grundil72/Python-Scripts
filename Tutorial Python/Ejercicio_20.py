# Exercise 20: From the train.csv file, we want to locate those homes that have 3 or more bedrooms, 2 or more full bathrooms, at least one half bathroom, 
# a neighborhood other than CollgCr, and their sales price is between 150000 and 300000. We are interested in finding out the following information:

# The complete list.
# Of them, get a list by neighborhood and number of bathrooms.
# The total number of dwellings in our table.
# the average of the house prices in our table.

import pandas as pd

df = pd.read_csv('train.csv')

df.info()
print(df.columns)

print("\nListado completo")
bed = df[df['BedroomAbvGr'] >=3]
print(bed)
completList = df[(df['BedroomAbvGr'] >=3) & (df['FullBath'] >=2) & (df['HalfBath'] >=1) & (df['Neighborhood'] != 'CollgCr') & df["SalePrice"].between(150000, 300000) ]
print(completList)

print("\nListado agrupado")
group = list(completList.groupby(by =["Neighborhood", "BedroomAbvGr"]).groups)
print(group)

total_viviendas = len(completList)
print(f"\nTotal de viviendas: {total_viviendas}")

print(f"\nMedia de precios de mi lista: {completList.SalePrice.mean()}")