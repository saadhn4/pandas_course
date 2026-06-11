import pandas as pd

# ****** DAY 1 PRACTICE - SERIES *****

# Tasks:

# Print the entire Series.
# Print Tuesday's temperature using .loc.
# Print Thursday's temperature using .iloc.

# data = [28, 31, 29, 35]

# temperatures = pd.Series(data, index=["Mon", "Tue", "Wed", "Thu"])

# print(temperatures)
# print(temperatures.loc["Tue"])
# print(temperatures.iloc[3])

# sales = {"Jan": 5000, "Feb": 6200, "Mar": 5800}

# Tasks:

# Create the Series.
# Print the sales for February.
# Print all months where sales are greater than 5500.

# series = pd.Series(sales)
# print(series)
# print(series.loc["Feb"])
# print(series[series >= 5500])

# stock = {"Apples": 50, "Bananas": 30, "Oranges": 40}

# Tasks:

# Convert it to a Series.
# Add 20 to the number of Bananas.
# Print the updated Series.

# series = pd.Series(stock)
# series.loc["Bananas"] += 20
# print(series)

# scores = [45, 72, 88, 35, 91]
# series = pd.Series(scores, index=["A", "B", "C", "D", "E"])

# Tasks:

# Create the Series.
# Print only the scores that are 70 or higher.
# Print only the scores that are less than 50.

# print(series)
# print(series[series >= 70])
# print(series[series < 50])

steps = {"Monday": 8000, "Tuesday": 12000, "Wednesday": 9500, "Thursday": 15000}

# Tasks:

# Create a Series.
# Print Wednesday's steps using .loc.
# Print Tuesday's steps using .iloc.
# Increase Monday's steps by 2000.
# Print only the days with 10,000 or more steps.

# series = pd.Series(steps)
# print(series)
# print(series.loc["Wednesday"])
# print(series.iloc[1])
# series.loc["Monday"] += 2000
# print(series)
# print(series[series >= 10000])
