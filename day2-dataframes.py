import pandas as pd

# A dataframe is a tabular data structure with rows and columns (2D)

data = {"Name": ["John", "Saad", "Saif"], "Age": [20, 21, 22]}

df = pd.DataFrame(data, index=["Emp1", "Emp2", "Emp3"])

# select a single row using loc and iloc
# print(df.loc["Emp1"])
# print(df.iloc[0])

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new row or new rows (easiest way = create a new df then concat it)
new_row = pd.DataFrame(
    [
        {"Name": "Sandy", "Age": 23, "Job": "Driver"},
        {"Name": "Eugene", "Age": 60, "Job": "Owner"},
    ],
    index=["Emp4", "Emp5"],
)

# [] bc we have to mention  df first
df = pd.concat([df, new_row])

print(df)
