import pandas as pd

df = pd.read_csv('data.csv')

print("Prints out 10 records")
print(df.head(10))

print("Prints default 5 records")
print(df.head())

print("Prints specified number of records from bottom")
print(df.tail())