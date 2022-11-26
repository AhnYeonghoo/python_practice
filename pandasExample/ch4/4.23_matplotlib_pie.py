import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('default')

df = pd.read_csv("./auto-mpg.csv" , header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'acceleration', 'model year', 'origin', 'name']

df['count'] = 1
print(df['count'])