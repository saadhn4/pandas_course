import pandas as pd

# Data cleaning = process of removing incomplete, irrelevant or incorrect data

# 75% of the work done with pandas is data cleaning

df = pd.read_csv("data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary"])
# print(df)

# 2. Handle missing data
# dropna = drop not available
# dropping entire row where theres no type2
# df = df.dropna(subset=["Type2"])

# Instead of NA this adds none
# df = df.fillna({"Type2": "None"})
# print(df)

# 3. Fix inconsitent values
# making grass and fire uppercase
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE"})
# print(df.to_string())

# 4. Standardize text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 5. Fix data types
# Instead of 0 and 1 it became true and false
# df["Legendary"] = df["Legendary"].astype(bool)
# print(df.to_string())

# 6. Remove duplicate values
# i copy pasted bulbasur row like 4 times
df = df.drop_duplicates()

print(df.to_string())
