import pandas as pd

df = pd.read_csv('dirtydata.csv')

# Dropna returns new DataFrame and does not change the original
new_df = df.dropna()

print(new_df.to_string())

# Will change the original DataFrame inplace true does not return new DataFrame but removes all null values
df.dropna(inplace=True)

print(df.to_string())

# Fillna replaces all the empty values
df.fillna(130, inplace=True)

print(df)


# Will replace all null values only in Calories column
df["Calories"].fillna(130, inplace=True)

# Calculates respective values for specified column can use mean()/ median()/ mode()

# Mean is average value (Sum of all values divided by number of values)
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace=True)

# Median is the middle value, after all the values are sorted ascending
x = df["Calories"].median()

df["Calories"].fillna(x, inplace=True)

# Mode appears most frequently
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)

