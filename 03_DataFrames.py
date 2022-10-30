import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

a = pd.DataFrame(data)
print(a) 
print(a.loc[0])
print(a.loc[[0, 1]])