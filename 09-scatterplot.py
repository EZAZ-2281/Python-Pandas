import pandas as pd
import matplotlib.pyplot as sp

df = pd.read_csv('data.csv') 
# df.plot()
# sp.show() 
# ---
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories', color = 'red')
sp.show()
# ---
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# sp.show()