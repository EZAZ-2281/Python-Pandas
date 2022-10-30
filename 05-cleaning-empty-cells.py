import pandas as pd

df = pd.read_csv('data.csv')

# return a new data frame with no empty cells
# will not change the original
newdf = df.dropna()
print(newdf.to_string()) 

# this will change the original data frame
df.dropna(inplace = True) 
print(df) 

# replace null value with number 130
df.fillna(130, inplace = True)
print(df.to_string())

# replace null value in the age column with the value 12
df['age'].fillna(12, inplace = True)
print(df)

# find the mean of Caloried column
z = df['Calories'].mean()
z1 = df['Calories'].median()
z2 = df['Calories'].mode()
z2 = df['Calories'].mode()[0]
print(z)
print(z1)
print(z2)
