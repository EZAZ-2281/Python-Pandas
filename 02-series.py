import pandas as pd
item = [1 ,2 ,3, 4]
d = pd.Series(item) 
print(d) 

calories = {
    "day1": 420, 
    "day2": 380, 
    "day3": 390
}
x = pd.Series(calories)
print(x)