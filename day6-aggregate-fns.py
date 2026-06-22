import pandas as pd

# Aggregate fns = Reduce a set of values into a single summary valur

# Used to summarize and analyze data
# Often used with groupby() function

df = pd.read_csv("data.csv")

# **WHOLE DATAFRAME**
# Find the mean of any columns that are numeric
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))

# Counting the number of values in each column
# excludes null values
# print(df.count())

# **SINGLE COLUMN**
# print(df["Height"].mean())
# print(df["Weight"].sum())
# print(df["Height"].min())
# print(df["Height"].max())

group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
