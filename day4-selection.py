import pandas as pd

# Setting index col allows us to locate the pokemon by their name, instead of their index
df = pd.read_csv("data.csv", index_col="Name")

# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())

# Select multiple columns [[]]
# print(df[["Name", "Height", "Weight"]].to_string())

# SELECTION BY ROW/S
# print(df.loc["Bulbasaur"])

# If you want only specific columns do this
# print(df.loc["Bulbasaur", ["No", "Height"]])

# (slicing) displayes every pokemons no and height from bulb to pika
# print(df.loc["Bulbasaur":"Pikachu", ["No", "Height"]])

# print(df.iloc[0:11])

pokemon = input("Enter a pokemon's name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
