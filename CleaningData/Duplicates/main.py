import pandas as pd

df = pd.read_csv('dirtydata.csv')

print(df.duplicated())

# Remove duplicates

df.drop_duplicates(inplace=True)

print(df)