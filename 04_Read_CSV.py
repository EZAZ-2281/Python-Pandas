import pandas as pd

df = pd.read_csv('data.csv')
print(df) 

print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))

print(df.info())

""" The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason. """


