# Series = A Pandas 1_Dimensional labeled array that can hold any data type
#             Think of it like a single column in a spreadsheet  (1-Dimensional)

# import pandas as pd
# print(pd.__version__)
# print("Hello")


# import pandas as pd
#
# data = [100, 234, 546, 754]   # int type data
# series = pd.Series(data)         # index start with 0, 1,2,3,4...
# series = pd.Series(data, index=["a", "b", "c", "d"])  # index start with a,b,c,d ...
# series = pd.Series(data, index=["AimGod", "Bull", "comrade", "Doom"])

# print(series)

# print(series.loc["a"])   # LockByLabel   # Output is :- 100
# print(series.loc["b"])   # LockByLabel   # Output is :- 234

# series.loc["c"] = 400    # Data Manipulation

# print(series.iloc[2])     # Integer-location based indexing

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