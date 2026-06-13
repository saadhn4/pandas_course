import pandas as pd

df = pd.read_csv("data.csv")

# For JSON - pd.read_json("data.json")

# Only gives first 5 and last 5
# print(df)

# prints everything
print(df.to_string())
