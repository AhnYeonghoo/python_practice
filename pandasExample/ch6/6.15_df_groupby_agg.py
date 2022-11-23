import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all);print('\n')
print(type(std_all));print('\n')

std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))

def min_max(x):
    return x.max() - x.min()
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())

agg_sep = grouped.agg(['min', 'max'])
print(agg_sep.head())
