import pandas as pd
import matplotlib.pyplot as histo

df = pd.read_csv('data.csv') 
df['Duration'].plot(kind = 'hist')
histo.show()