import pandas

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pandas.DataFrame(data)

print(df)
print('---------------------')
print(df.loc[0])
print('---------------------')
print(df.loc[[0, 1]])
print('---------------------')  

dfd = pandas.DataFrame(data, index=["day1", "day2", "day3"])
print(dfd)

print(dfd.loc["day2"])

csvData= pandas.read_csv('data.csv')

print(csvData)