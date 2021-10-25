import pandas as pd
a = [1, 7, 2]

varSeries = pd.Series(a)

print(varSeries)
print(varSeries[0])

varSeriesCustom = pd.Series(a, index=["x", "y", "z"])
print(varSeriesCustom)
print(varSeriesCustom[0])

calories = {"day1": 420, "day2": 380, "day3": 390}

varCalories = pd.Series(calories)
print(varCalories)


varSelectedDay = pd.Series(calories, index=["day1", "day2"])

print(varSelectedDay)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

varData = pd.DataFrame(data)

print(data)

