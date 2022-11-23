import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement',
              'horsepower', 'weight', 'acceleration',
              'model year', 'origin', 'name']

df[['mpg', 'cylinders']].plot(kind='box')
plt.show()