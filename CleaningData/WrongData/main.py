import pandas as pd

df = pd.read_csv('dirtydata.csv')

# Inserts new value in selected row
df.loc[7, 'Duration'] = 45

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

print(df)

# Remove values that are less than selected

for x in df.index:
    if df.loc[x, "Duration"] < 60:
        df.drop(x, inplace=True)
        
print(df)