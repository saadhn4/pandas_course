import pandas as pd

# Series = A pandas 1D labelled array that can hold any data type. Think of it like a single column in a spreadsheet

# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["a", "b", "c", "d", "e"])


# This returns 100 (b would return 102 and so on)
# print(series.loc["a"])

# this changes 104 to 200
# series.loc["c"] = 200

# This returns 100
# print(series.iloc[0])

# print(series)

# prints d and e
# print(series[series >= 200])

calories = {"day 1": 1750, "day 2": 2100, "day 3": 1700}

series = pd.Series(calories)

# print(series.loc["day 1"])

# series.loc["day 3"] += 500

# print(series[series >= 2000])
