# Series = A Pandas 1_Dimensional labeled array that can hold any data type
#             Think of it like a single column in a spreadsheet  (1-Dimensional)
import typer.cli
# import pandas as pd

# print(pd.__version__)
# print("Hello")

# data = [100, 234, 546, 754]   # int type data
# series = pd.Series(data)         # index start with 0, 1,2,3,4...

# series = pd.Series(data, index=["a", "b", "c", "d"])  # index start with a,b,c,d ...

# series = pd.Series(data, index=["AimGod", "Bull", "comrade", "Doom"])

# print(series)

# print(series.loc["a"])   # LockByLabel   # Output is :- 100
# print(series.loc["b"])   # LockByLabel   # Output is :- 234

# series.loc["c"] = 400    # Data Manipulation
# print(series)
# print(series.iloc[2])     # Integer-location based indexing
# print(series.loc["c"])     # Integer-location based indexing

# data1 = [100.3, 234.23, 546.6, 754.7]
# series = pd.Series(data1)        # float type data

# data2 = ['A', 'B', 'C', 'D']
# data2 = ['Apple', 'Banana', 'Commatozze', 'Danny']
# series = pd.Series(data2)        # str type data

# data3 = [True, False, True, False, False]
# series = pd.Series(data3)        # Boolean type data


# data1 = [100, 234.23, "J", True, "Help"]
# series = pd.Series(data1)        # Object type data
# print(series)

# ---------------------------------------------------------------------

# date = [123, 5443, 676]
# date = ["C", 123, 5443, 676]
# date = ["Come", "Bitch"]
#
# series = pd.Series(date)
# print(series)

# q = pd.Series(range(0, 7, 2))
# q = pd.Series(["apple", "banana", "orange"], name="fruit")

# q = pd.DataFrame([
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8], ])

# q = pd.DataFrame([ [0, 1, 2], [3, 4, 5], [6, 7, 8], ])
# print(q)

# ---------------------------------13th May 2026 ------------------------------------

        # Filter Data

# import pandas as pd
#
# data = [100, 234, 546, 754]   # int type data
# series = pd.Series(data, index=["a", "b", "c", "d"])  # index start with a,b,c,d ...
#
# print(series[series >= 500])  # Filter Data

# Calculator for Calories consumed per Days

# import pandas as pd
from scipy.constants import calorie

# calories = {"Mon" : 2400, "Tues" : 2490, "Wed" : 2500, "Thus" : 2700, "Fri" : 2900, "Sat" : 2690, "Sun" : 4000}
# series = pd.Series(calories)

# print(series)

# print(series.loc["Tues"])

# series.loc["Tues"] += 900  # When i eat more than any Tues

# print(series.loc["Tues"])

# Filter Data

# print(series[series >= 2700])
# print(series[series < 2700])

# ------------------------------------------------------
         # Questions

# pokemons = ["Bulbasaur", "lvysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard"]
# series = pd.Series(pokemons, index=[1,2,3,4,5,6])
# series = pd.Series(pokemons)
# print(series)


# import pandas as pd

# pokemon_names = ['Bulbasaur', 'lvysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard']
# custom_index = [1,2,3,4,5,6]
#
# pokemon_series = pd.Series(pokemon_names, index=custom_index)
#
# print(pokemon_series)


# data = {
#     'pokemon' : ['Bulbasaur', 'lvysaur', 'Venusaur',
#                  'Charmander', 'Charmeleon', 'Charizard']
# }
# df = pd.DataFrame(data)
# df.index = df.index + 1
#
# print(df)
# print(df.type)

# Problem is this is "str" Type not "Object" Type

# ---------------- DataFrames -----------------

# DataFrames = A tabular data structure with rows AND columns. (2 Dimensional
              # it's similar to an Excel Spreadsheet
#
# import pandas as pd
#
# data = {
#     "Name" : ["KimjongUng", "PingPongUng", "JethaJungUng"],
#     "Age" : [48, 39, 59]
# }

# df = pd.DataFrame(data)
# print(df)

# df = pd.DataFrame(data, index=["President", "Vice-President", "Supreme"])
# print(df)
# print(df.loc["Supreme"])
# print(df.iloc[2])

# Add a new column

# df["Strength"] = ["Non Human", "gOD level", "Invincible"]
# print(df)

# ----------- Add a new Row -------------

# new_row = pd.DataFrame([{"Name" : "Xinjong", "Age" : "56", "Strength" : "Human Level"}]
#                        , index=["Chinese"])
# df = pd.concat([df, new_row])
# print(df)

# ----------- Add new Rows -------------
#
# new_rows = pd.DataFrame([{"Name" : "Xinjong", "Age" : "56", "Strength" : "Human Level"},
#                         {"Name": "Hisuka", "Age": "19", "Strength": "InHuman Level"}],
#                        index=["Chinese","Japanese"])
# df = pd.concat([df, new_rows])
# print(df)

# ---------------- Importing -----------------

# CSV = Comma-separated values
# JSON = JavaScript Object Notation

import pandas as pd

df = pd.read_csv("data.csv") # For CSV file
# df = pd.read_json("data.json") # For JSON file
# print(df)
print(df.to_string()) # For Print EveryThing in Data File