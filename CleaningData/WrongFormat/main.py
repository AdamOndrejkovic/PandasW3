import pandas as pd

df = pd.read_csv('dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

# Removing rows with non Date and Time value

df.dropna(subset=['Date'], inplace=True)
print(df)